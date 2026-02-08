# convex_db.py
"""
Convex-backed user storage for CalmMateAI.
Uses the same interface as database.py so app.py can switch via CONVEX_URL.
Requires: pip install convex python-dotenv, and a Convex project (convex/ + npx convex dev).
"""
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Optional: use Convex only when CONVEX_URL is set
_convex_client = None


def _get_client():
    global _convex_client
    if _convex_client is None:
        try:
            from convex import ConvexClient
            url = os.getenv("CONVEX_URL")
            if not url:
                raise ValueError("CONVEX_URL is not set")
            _convex_client = ConvexClient(url)
        except Exception as e:
            raise RuntimeError(
                "Convex not configured. Install: pip install convex. "
                "Set CONVEX_URL in .env and run 'npx convex dev' to create the backend."
            ) from e
    return _convex_client


def get_registered_users():
    """
    Return all users as { email: { 'name': str, 'password': str } }.
    Passwords in Convex are stored hashed; this returns the hash for check_password.
    """
    client = _get_client()
    rows = client.query("users:list")
    return {r["email"]: {"name": r["name"], "password": r["password"]} for r in (rows or [])}


def get_user_name(email):
    """Return display name for email, or 'User' if not found."""
    client = _get_client()
    user = client.query("users:getByEmail", {"email": email})
    return user["name"] if user else "User"


def save_user(email, name, password):
    """Register a new user. Password is hashed before sending to Convex."""
    password_hash = generate_password_hash(password)
    client = _get_client()
    try:
        client.mutation("users:create", {
            "email": email,
            "name": name,
            "password": password_hash,
        })
    except Exception as e:
        if "already registered" in str(e).lower() or "unique" in str(e).lower():
            raise ValueError("Email already registered") from e
        raise


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
    client = _get_client()
    args = {"email": email, "newName": new_name}
    if new_password is not None:
        args["newPassword"] = generate_password_hash(new_password)
    result = client.mutation("users:update", args)
    return result is not None
