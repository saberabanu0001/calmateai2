# 🌿 CalmMateAI - Complete Beginner's Guide

## 📖 What is CalmMateAI?

**CalmMateAI** is a **web application** (like a website) that helps people with their mental health and well-being. Think of it like a friendly chatbot that:
- Listens to your problems
- Gives supportive advice
- Helps you find emergency contacts
- Provides resources for mental health

---

## 🌐 What is a Web Application?

A **web application** is a program that runs on the internet. When you visit a website like Facebook or Gmail, you're using a web application.

**How it works:**
1. **You (the user)** open a web browser (Chrome, Safari, etc.)
2. **Your browser** sends a request to a **server** (a computer somewhere on the internet)
3. **The server** processes your request and sends back a **web page**
4. **Your browser** displays the web page

**CalmMateAI** is a web application that runs on a server and shows you web pages in your browser.

---

## 🏗️ How is CalmMateAI Built?

CalmMateAI has **two main parts**:

### 1. **Backend (The Brain)** 🧠
- **What it is**: The server-side code that does the thinking
- **Technology**: Python + Flask
- **What it does**:
  - Handles user requests
  - Talks to AI (Groq API)
  - Stores user data
  - Processes information

### 2. **Frontend (The Face)** 😊
- **What it is**: What you see in your browser
- **Technology**: HTML, CSS, JavaScript
- **What it does**:
  - Shows the user interface
  - Makes it look pretty
  - Handles user interactions (clicks, typing, etc.)

---

## 📁 Project Structure Explained

Let me explain what each folder and file does:

```
CalmMateAI/
│
├── app.py                    ← THE MAIN FILE (The heart of the app)
├── requirements.txt          ← List of Python packages needed
├── .env                      ← Secret keys (API keys, passwords)
│
├── templates/                 ← HTML pages (what users see)
│   ├── dashboard.html        ← Main page after login
│   ├── chat_page.html        ← Chat interface
│   ├── login.html            ← Login page
│   ├── register.html         ← Sign up page
│   └── ...
│
├── static/                   ← CSS and JavaScript files
│   ├── css/style.css         ← Makes pages look pretty
│   └── js/chat_script.js     ← Makes chat interactive
│
├── emergency_contacts.py      ← Finds emergency contacts
├── seriousness_detector.py    ← Detects how serious user's issue is
├── suggestions_manager.py    ← Provides helpful suggestions
├── university_auth.py        ← Handles university login
│
├── emergency_data.json       ← Database of emergency contacts
├── university_data.json      ← Database of university resources
├── users.json                ← Stores registered users
│
└── venv/                     ← Virtual environment (Python packages)
```

---

## 🔑 Key Files Explained

### 1. **app.py** - The Main Controller
**Think of it as**: The brain that controls everything

**What it does**:
- Creates the Flask web server
- Defines all the routes (URLs like `/login`, `/chat`, etc.)
- Handles user requests
- Connects to AI APIs
- Returns responses

**Key parts**:
```python
@app.route('/chat')  # When user visits /chat, show chat page
def chat():
    return render_template('chat_page.html')

@app.route('/api/chat', methods=['POST'])  # When user sends message
def chat_api():
    # Get user's message
    # Send to AI
    # Return AI response
```

### 2. **templates/** - The Web Pages
**Think of it as**: The pages of a book

**What it does**:
- Contains HTML files (the structure of web pages)
- Each file is a different page users can visit
- Uses Jinja2 templating (allows dynamic content)

**Example**: `chat_page.html` is the chat interface you see

### 3. **static/** - The Styling & Interactivity
**Think of it as**: The makeup and animations

**What it does**:
- **CSS files**: Make pages look beautiful (colors, fonts, layout)
- **JavaScript files**: Make pages interactive (buttons work, chat updates)

### 4. **requirements.txt** - Dependencies
**Think of it as**: A shopping list

**What it does**:
- Lists all Python packages the app needs
- When you run `pip install -r requirements.txt`, it installs everything

**Key packages**:
- `Flask` - Web framework (makes web apps)
- `gunicorn` - Server to run the app
- `langchain-groq` - Connects to Groq AI
- `python-dotenv` - Loads environment variables

### 5. **JSON Files** - Databases
**Think of it as**: Filing cabinets storing information

**What they do**:
- `users.json` - Stores registered users (email, password, name)
- `emergency_data.json` - Stores emergency contacts by location
- `university_data.json` - Stores university resources

---

## 🔄 How the App Works (Step by Step)

### Scenario: User wants to chat with AI

1. **User opens browser** → Types `http://localhost:5001/chat`

2. **Browser sends request** → "Hey server, show me the chat page!"

3. **app.py receives request** → Sees route `/chat`

4. **app.py runs function**:
   ```python
   @app.route('/chat')
   def chat():
       return render_template('chat_page.html')
   ```

5. **Server sends HTML** → Browser receives `chat_page.html`

6. **Browser displays page** → User sees the chat interface

7. **User types message** → "I'm feeling sad"

8. **JavaScript sends to server** → POST request to `/api/chat`

9. **app.py processes**:
   - Gets the message
   - Sends to Groq AI API
   - Gets AI response
   - Returns to browser

10. **Browser shows response** → User sees AI's reply

---

## 🛠️ Technologies Used (Simple Explanation)

### **Python**
- **What**: A programming language (like English, but for computers)
- **Why**: Easy to learn, powerful, great for web apps

### **Flask**
- **What**: A Python framework (a toolkit for building web apps)
- **Why**: Simple, flexible, perfect for beginners

### **HTML**
- **What**: The structure of web pages (like the skeleton)
- **Why**: Every website uses it

### **CSS**
- **What**: Makes pages look pretty (colors, fonts, layout)
- **Why**: Without it, pages would be plain text

### **JavaScript**
- **What**: Makes pages interactive (buttons work, things move)
- **Why**: Makes the app feel alive

### **JSON**
- **What**: A way to store data (like a spreadsheet)
- **Why**: Easy to read and write

### **Groq API**
- **What**: An AI service (gives intelligent responses)
- **Why**: Makes the chatbot smart

---

## 🚀 How to Run the Project (Step by Step)

### Step 1: Install Python
- Download from python.org
- Make sure it's Python 3.8 or higher

### Step 2: Open Terminal/Command Prompt
- **Mac**: Open Terminal app
- **Windows**: Open Command Prompt or PowerShell

### Step 3: Navigate to Project Folder
```bash
cd "/Users/saberabanu/All Drives/Personal/CalmateAI"
```

### Step 4: Create Virtual Environment
```bash
python3 -m venv venv
```
**What this does**: Creates an isolated Python environment (like a separate room for your project)

### Step 5: Activate Virtual Environment
```bash
# Mac/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```
**What this does**: Activates the isolated environment (enters the room)

### Step 6: Install Dependencies
```bash
pip install -r requirements.txt
```
**What this does**: Installs all Python packages needed (like installing apps on your phone)

### Step 7: Create .env File
Create a file named `.env` with:
```
FLASK_SECRET_KEY=your-secret-key-here
GROQ_API_KEY=your-groq-api-key
PORT=5001
```

### Step 8: Run the App
```bash
python app.py
```

### Step 9: Open Browser
Go to: `http://localhost:5001`

**🎉 The app is now running!**

---

## 🎯 Main Features Explained

### 1. **User Registration & Login**
- Users create accounts
- Data stored in `users.json`
- Session management (remembers you're logged in)

### 2. **AI Chat**
- User types message
- Sent to Groq AI API
- AI responds with supportive message
- Shows seriousness level and suggestions

### 3. **Emergency Contacts**
- User enters location (country, city)
- App searches `emergency_data.json`
- Shows relevant contacts

### 4. **University Resources**
- User enters university name
- App searches `university_data.json`
- Shows university-specific resources

### 5. **Profile Management**
- Users can update their name
- Change password
- View account info

---

## 🔐 Important Concepts

### **Environment Variables (.env)**
- **What**: Secret information (API keys, passwords)
- **Why**: Keeps secrets safe, not in code
- **Example**: `GROQ_API_KEY=abc123`

### **Routes**
- **What**: URLs that do different things
- **Examples**:
  - `/` → Home page
  - `/login` → Login page
  - `/chat` → Chat page
  - `/api/chat` → API endpoint (sends/receives data)

### **Sessions**
- **What**: Remembers you're logged in
- **How**: Stores info in cookies
- **Why**: So you don't have to login every time

### **API Endpoints**
- **What**: URLs that return data (not HTML pages)
- **Example**: `/api/chat` returns JSON data (AI response)
- **Used by**: JavaScript to update page without refreshing

---

## 🐛 Common Issues & Solutions

### **"Module not found" error**
- **Problem**: Python package not installed
- **Solution**: Run `pip install -r requirements.txt`

### **"Port already in use"**
- **Problem**: Another app using port 5001
- **Solution**: Change PORT in .env to 5002 or 5003

### **"API key invalid"**
- **Problem**: Wrong API key in .env
- **Solution**: Check your .env file has correct keys

### **"Can't connect to server"**
- **Problem**: App not running
- **Solution**: Make sure you ran `python app.py`

---

## 📚 Learning Path

If you're completely new, learn in this order:

1. **HTML Basics** → Understand web page structure
2. **CSS Basics** → Learn to style pages
3. **JavaScript Basics** → Make pages interactive
4. **Python Basics** → Learn programming fundamentals
5. **Flask Tutorial** → Learn web framework
6. **This Project** → Understand how it all connects

**Great Resources**:
- **HTML/CSS/JS**: w3schools.com
- **Python**: python.org (official tutorial)
- **Flask**: flask.palletsprojects.com

---

## 🎓 Key Takeaways

1. **Web apps have two parts**: Frontend (what you see) + Backend (the logic)

2. **Flask routes** connect URLs to functions

3. **Templates** are HTML pages with dynamic content

4. **JSON files** store data (like a simple database)

5. **APIs** let your app talk to external services (like Groq AI)

6. **Environment variables** keep secrets safe

---

## 💡 Next Steps

1. **Read the code** → Start with `app.py`, understand each route
2. **Modify something** → Change a color, add a button
3. **Add a feature** → Maybe a new page or function
4. **Deploy it** → Put it online so others can use it

**Remember**: Every expert was once a beginner. Take it one step at a time! 🚀

---

## ❓ Questions to Ask Yourself

As you explore the code, ask:
- "What does this function do?"
- "Why is this code here?"
- "What happens if I change this?"
- "How does this connect to that?"

**The best way to learn is by doing!** Try changing things and see what happens.

---

**Good luck on your coding journey! 🌟**
