# 🚀 QueryMate: SQL Query Assistant  

QueryMate is an interactive **text-to-SQL chatbot** that converts natural language queries into **SQL commands** and executes them on an **SQLite database**. Built with Python, it leverages the **Groq API** for natural language processing, making database querying easy and intuitive.  

---

## ✨ Features  
✅ Convert plain English queries into SQL statements  
✅ Execute SQL queries directly on an **SQLite database**  
✅ Supports multiple example databases (`chinook.db`, `test.db`)  
✅ Secure API key integration using environment variables  

---

## 📥 Installation  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/yashag24/querymate.git
cd querymate
```

2️⃣ **Create & activate a virtual environment**  
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

---

## 🌍 Environment Setup  

1️⃣ **Create a `.env` file** in the project root:  
```bash
touch .env
```
2️⃣ **Add your API key** to the `.env` file:  
```
GROQ_API_KEY=your_groq_api_key_here
```

3️⃣ **Ensure SQLite databases are available:**  
   - `chinook.db` (sample music database)  
   - `test.db` (your test database)  

---

## 🛠️ Usage  

Run QueryMate:  
```bash
python app.py
```

### Example Interaction:  
```
User: How many tracks are in the 'Rock' genre?
Bot: SELECT COUNT(*) FROM tracks WHERE genre = 'Rock';
Result: 200
```
To exit, type `exit`.  

---

🚀 **QueryMate** — Making SQL Queries Effortless! 🎯  

---

Let me know if you need more changes! 🚀
