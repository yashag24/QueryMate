# 🚀 QueryMate: AI-Powered SQL Query Assistant

QueryMate is an intelligent chatbot that transforms natural language queries into precise SQL statements and executes them on an SQLite database. Powered by Python and the Groq API, it streamlines database interactions, making SQL querying effortless and intuitive.

---

## 🌐 Deployment

QueryMate is deployed on **Render** and can be accessed here:\
🔗 **[Live Demo](https://querymate.onrender.com/)**

To deploy your own version, consider using **Render, Vercel, or AWS**.

---

## ✨ Features

✅ Convert plain English queries into SQL statements\
✅ Execute SQL queries directly on an **SQLite database**\
✅ Supports multiple example databases (`chinook.db`, `test.db`)\
✅ Secure API key integration using environment variables\
✅ **Web Deployment:** Live demo at **[QueryMate](https://querymate.onrender.com/)**

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

Run QueryMate locally:

```bash
python app.py
```

### Example Interaction:

```
User: How many tracks are in the 'Rock' genre?
Bot: SELECT COUNT(*) FROM tracks WHERE genre = 'Rock';
Result: 200
```



🚀 **QueryMate** — Making SQL Queries Effortless! 🎯

