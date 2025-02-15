from flask import Flask, render_template, request, jsonify, g, send_from_directory
import sqlite3
import json
import os
import re
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Fetch API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Set it in the .env file.")

# Initialize Groq client
client = Groq(api_key=api_key)

# Global variable to store current database file
current_db = "chinook.db"  # Default DB

def convert_sql_to_db(sql_file, db_file):
    with open(sql_file, "r", encoding="utf-8") as file:
        sql_script = file.read()

    sql_script = re.sub(r",\s*KEY .*?\(.*?\)", "", sql_script, flags=re.IGNORECASE)
    sql_script = re.sub(r"CREATE DATABASE .*?;", "", sql_script, flags=re.IGNORECASE)
    sql_script = re.sub(r"USE .*?;", "", sql_script, flags=re.IGNORECASE)
    sql_script = re.sub(r"AUTO_INCREMENT", "AUTOINCREMENT", sql_script, flags=re.IGNORECASE)

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.executescript(sql_script)
        conn.commit()
        return {"message": f"Database {db_file} created successfully."}
    except sqlite3.Error as e:
        return {"error": f"SQL execution failed: {e}"}
    finally:
        conn.close()

def connect_db():
    """Reuses the SQLite database connection for efficiency."""
    if 'db_conn' not in g:
        g.db_conn = sqlite3.connect(current_db)
    return g.db_conn

@app.teardown_appcontext
def close_db(error):
    """Closes the database connection when the request ends."""
    db_conn = g.pop('db_conn', None)
    if db_conn is not None:
        db_conn.close()

def execute_query(query):
    """Executes an SQL query and returns results."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description] if cursor.description else []
        return results, column_names
    except sqlite3.OperationalError as e:
        return f"SQL syntax error: {e}", []
    except sqlite3.IntegrityError as e:
        return f"Integrity constraint failed: {e}", []
    except sqlite3.Error as e:
        return f"Database error: {e}", []

def get_table_info():
    """Retrieves table structure from the current database."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    table_info = {}
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        table_info[table_name] = [(col[1], col[2]) for col in columns]
    return table_info

@app.route("/", methods=["GET"])
def home():
    """Renders the homepage."""
    index_path = os.path.abspath("templates/index.html")
    if not os.path.exists(index_path):
        return jsonify({"error": "index.html is missing"}), 500
    return render_template("index.html")

@app.route("/test")
def test():
    return "Flask is working!"

@app.route("/static/<path:filename>")
def serve_static(filename):
    """Serve static files (CSS, JS)."""
    return send_from_directory("static", filename)

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handles file uploads (.sql or .db)."""
    global current_db
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    if filename.endswith(".sql"):
        new_db = file_path.replace(".sql", ".db")
        response = convert_sql_to_db(file_path, new_db)
        os.remove(file_path)
        if "error" in response:
            return jsonify(response), 400
        current_db = new_db
    elif filename.endswith(".db"):
        current_db = file_path
    else:
        return jsonify({"error": "Invalid file format. Upload .sql or .db"}), 400

    return jsonify({"message": f"Database set to {current_db}"}), 200

@app.route("/query", methods=["POST"])
def query():
    user_input = request.json.get("query")
    if not user_input:
        return jsonify({"error": "No query provided"}), 400

    table_info = get_table_info()
    system_content = """You are an SQL assistant. Convert user queries into valid SQLite SQL statements.
    Output should always be a JSON object in this format:
    {"query": "SQL_QUERY_HERE"}
    Tables in the database: """ + str(table_info)

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
            response_format={"type": "json_object"},
        )
        response_json = json.loads(chat_completion.choices[0].message.content)
        sql_query = response_json.get("query")
        results, columns = execute_query(sql_query)

        if isinstance(results, str):
            return jsonify({"error": results})

        formatted_output = "<table border='1' style='width:100%; border-collapse: collapse;'>"
        if columns:
            formatted_output += "<tr>" + "".join(f"<th>{col}</th>" for col in columns) + "</tr>"
        for row in results:
            formatted_output += "<tr>" + "".join(f"<td>{str(cell)}</td>" for cell in row) + "</tr>"
        formatted_output += "</table>" if results else "<p>No results found.</p>"

        return jsonify({"query": sql_query, "results": formatted_output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
