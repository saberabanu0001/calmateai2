# 🌿 CalmMateAI

**Your personal well-being companion** — a web app that offers empathetic AI chat, seriousness detection, and quick access to mental health and crisis resources.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| **🤖 AI chat** | Supportive conversations powered by Groq (Llama). Fallback responses when API is unavailable. |
| **⚖️ Seriousness detection** | Estimates emotional severity and surfaces tailored suggestions. |
| **📍 Emergency contacts** | Search crisis hotlines and mental health contacts by country and city. |
| **🎓 University resources** | Look up counseling and wellness info for supported universities. |
| **📚 Well-being resources** | Curated tips and links for meditation, self-care, and professional help. |
| **👤 Profile & settings** | Update name and password; session-based login. |
| **🎙️ Voice input** | Optional speech-to-text in the chat (browser). |

---

## 🛠️ Tech stack

- **Backend:** Python 3, Flask  
- **AI:** Groq API (Llama 3.1)  
- **Frontend:** HTML, Tailwind CSS, JavaScript  
- **Data:** JSON (users, emergency data, university data)  
- **Server:** Gunicorn (production)

---

## 🚀 Quick start

### Prerequisites

- **Python 3.8+**
- **pip**

### 1. Clone and enter the project

```bash
git clone https://github.com/saberabanu0001/NewCalmateAI.git
cd NewCalmateAI
```

### 2. Create and activate a virtual environment

```bash
# Create
python3 -m venv venv

# Activate — macOS/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Copy `env_template.txt` to `.env` and set:

```env
FLASK_SECRET_KEY=your-secret-key-here
GROQ_API_KEY=your-groq-api-key
PORT=5001
```

Generate a secret key:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 5. Run the app

```bash
python app.py
```

Then open **http://localhost:5001** (or the port in `PORT`).

---

## 📁 Project structure

```
CalmMateAI/
├── app.py                 # Flask app, routes, API
├── requirements.txt      # Python dependencies
├── Procfile               # Production start (Gunicorn)
├── runtime.txt            # Python version (e.g. for Render)
│
├── templates/             # HTML (Jinja2)
│   ├── base.html
│   ├── dashboard.html
│   ├── chat_page.html
│   ├── login.html, register.html
│   ├── emergency_contacts.html
│   ├── university_access.html
│   ├── wellbeing_resources.html
│   └── profile.html
│
├── static/
│   ├── css/style.css
│   └── js/chat_script.js
│
├── emergency_contacts.py   # Location-based contacts
├── seriousness_detector.py # Emotional severity
├── suggestions_manager.py  # Recovery suggestions
├── university_auth.py      # University resources
├── voice_input.py          # Speech handling
│
├── emergency_data.json     # Crisis/mental health contacts
├── university_data.json    # University wellness info
├── university_students.json
└── users.json              # User accounts (created at runtime)
```

---

## 🔧 Configuration

| Variable | Required | Description |
|----------|----------|-------------|
| `FLASK_SECRET_KEY` | Yes | Session encryption; use a long random string. |
| `GROQ_API_KEY` | For AI chat | From [Groq Console](https://console.groq.com). Without it, built-in fallback responses are used. |
| `PORT` | No | Server port (default 5001). |
| `CONVEX_URL` | No | If set, user data is stored in [Convex](https://convex.dev) instead of SQLite. See [CONVEX_SETUP.md](CONVEX_SETUP.md). |

---

## 🌐 Deploying

- **Render:** See [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step Render (and other) deployment.
- **Start command:** `gunicorn app:app` (or use the `Procfile`).
- Set `FLASK_ENV=production` and the env vars above in your host’s dashboard.

---

## 📖 Documentation

- **[BEGINNER_GUIDE.md](BEGINNER_GUIDE.md)** — Concepts, structure, and learning path for new developers.
- **[DEPLOYMENT.md](DEPLOYMENT.md)** — Deploy to Render, Railway, or Fly.io.

---

## 🧪 Run from VS Code

- **Run/Debug:** Use the “Run CalmMateAI Flask App” configuration (F5).
- **Task:** Run task “Start CalmMateAI Flask App” to start the server from the terminal.

---

## 📄 License

This project is for educational and personal use. Use crisis and emergency features responsibly; they do not replace professional care.

---

## 👩‍💻 Author

**Sabera Banu** — Initial development and design of CalmMateAI.

CalmMateAI is built with the goal of supporting mental well-being through approachable technology.
