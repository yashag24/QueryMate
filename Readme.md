# 🚀 QueryMate: SQL Query Assistant  

QueryMate is an interactive **text-to-SQL chatbot** that converts natural language queries into **SQL commands** and executes them on an **SQLite database**. Built with Python, it leverages the **Groq API** for natural language processing, making database querying easy and intuitive.  

---

## ✨ Features  
✅ Convert plain English queries into SQL statements  
✅ Execute SQL queries directly on an **SQLite database**  
✅ Display structured results in a user-friendly format  
✅ Secure API key integration using environment variables  

---

## 📖 Table of Contents  
- [⚙️ Prerequisites](#⚙️-prerequisites)  
- [📥 Installation](#📥-installation)  
- [🌍 Environment Setup](#🌍-environment-setup)  
- [🛠️ Usage](#🛠️-usage)  
- [🤝 Contributing](#🤝-contributing)  

---

## ⚙️ Prerequisites  

Before installing QueryMate, ensure you have the following installed:  

🔹 **Python 3.7+** 🐍  
🔹 **SQLite** (pre-installed with Python) 🗄️  
🔹 **Groq API Key** 🔑 (for NLP processing)  
🔹 **Virtual Environment** (recommended for package management)  

---

## 📥 Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/querymate.git
cd querymate
```

### 2️⃣ Create & activate a virtual environment  

💻 **For macOS/Linux:**  
```bash
python3 -m venv venv
source venv/bin/activate
```

🖥️ **For Windows:**  
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

---

## 🌍 Environment Setup  

QueryMate requires a **Groq API key** to process natural language queries.  

1. **Create a `.env` file** in the project root:  
```bash
touch .env
```
2. **Add your API key** to the `.env` file:  
```
GROQ_API_KEY=your_groq_api_key_here
```

3. Ensure your SQLite database (e.g., `chinook.db`) is available in the project directory.

---

## 🛠️ Usage  

Once installed, run QueryMate using:  
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

## 🤝 Contributing  

We welcome contributions! To contribute:  

1. **Fork** the repository  
2. **Create a new branch** (`git checkout -b feature-branch`)  
3. **Commit your changes** (`git commit -m "Add new feature"`)  
4. **Push to your branch** (`git push origin feature-branch`)  
5. **Submit a Pull Request** 🚀  

---

🚀 **QueryMate** — Making SQL Queries Effortless! 🎯  

---

### 🔹 **Corrections & Improvements:**  
✔ Fixed broken section links  
✔ Corrected Windows activation command  
✔ Improved formatting for clarity  

Let me know if you need any more tweaks! 🚀
