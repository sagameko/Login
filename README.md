# 🔐 Streamlit Login Examples

This repository contains **three examples of login systems built with Streamlit**:

1. **Simple Login** – Hardcoded username and password (for learning).
2. **SQLite Login** – Database authentication using SQLite.
3. **Google OAuth Login** – Sign in with Google using OAuth 2.0.

These examples are designed for learning purposes so you can gradually move from a basic login form to a real-world authentication system.

---

## 📂 Repository Structure

login-demo/
│
├── 1_simple_login/
│ └── app.py
│
├── 2_sqlite_login/
│ ├── db_setup.py
│ └── app.py
│
├── 3_google_login/
│ └── Login.py
│
├── requirements.txt
└── README.md


---

## 📦 Installation

Clone this repository and set up a virtual environment:

```bash
git clone https://github.com/YOUR_USERNAME/login-demo.git
cd login-demo

# Create virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
