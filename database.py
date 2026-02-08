# database.py
"""
SQLite database for user storage.
Uses hashed passwords; compatible with existing app routes.
"""
import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Database file path (in project root)
DB_PATH = os.path.join(os.path.dirname(__file__), "calmateai.db")


def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # access columns by name
    return conn


def init_db():
    """Create the users table if it doesn't exist."""
    conn = get_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
    finally:
        conn.close()


def get_registered_users():
    """
    Return all users as a dict: { email: { 'name': str, 'password': str } }.
    Keeps the same shape as the old users.json for compatibility.
    Passwords in DB are hashed; this returns the hash (only for checking via check_password).
    """
    init_db()
    conn = get_connection()
    try:
        rows = conn.execute("SELECT email, name, password FROM users").fetchall()
        return {row["email"]: {"name": row["name"], "password": row["password"]} for row in rows}
    finally:
        conn.close()


def get_user_name(email):
    """Return display name for email, or 'User' if not found."""
    init_db()
    conn = get_connection()
    try:
        row = conn.execute("SELECT name FROM users WHERE email = ?", (email,)).fetchone()
        return row["name"] if row else "User"
    finally:
        conn.close()


def save_user(email, name, password):
    """
    Register a new user. Password is hashed before storing.
    Raises if email already exists (caller should check first).
    """
    init_db()
    password_hash = generate_password_hash(password)
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO users (email, name, password) VALUES (?, ?, ?)",
            (email, name, password_hash),
        )
        conn.commit()
    finally:
        conn.close()


def check_password(email, password):
    """Return True if the given password matches the stored hash for this email."""
    users = get_registered_users()
    if email not in users:
        return False
    return check_password_hash(users[email]["password"], password)


def update_user(email, new_name, new_password=None):
    """
    Update name and optionally password for the given email.
    Returns True if a row was updated.
    """
    init_db()
    conn = get_connection()
    try:
        if new_password:
            password_hash = generate_password_hash(new_password)
            conn.execute(
                "UPDATE users SET name = ?, password = ? WHERE email = ?",
                (new_name, password_hash, email),
            )
        else:
            conn.execute("UPDATE users SET name = ? WHERE email = ?", (new_name, email))
        conn.commit()
        return conn.total_changes > 0
    finally:
        conn.close()
