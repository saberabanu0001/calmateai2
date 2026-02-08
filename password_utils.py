"""
Password hashing using only stdlib (hashlib + secrets).
Avoids werkzeug/ hashlib.scrypt so it works on Python builds without scrypt support.
"""
import base64
import hashlib
import secrets

ITERATIONS = 260000
SALT_BYTES = 16
HASH_BYTES = 32


def hash_password(password: str) -> str:
    """Return a stored hash string for the given password."""
    salt = secrets.token_bytes(SALT_BYTES)
    h = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS,
        dklen=HASH_BYTES,
    )
    b64_salt = base64.b64encode(salt).decode("ascii")
    b64_hash = base64.b64encode(h).decode("ascii")
    return f"pbkdf2_sha256${ITERATIONS}${b64_salt}${b64_hash}"


def check_password(stored: str, password: str) -> bool:
    """Return True if password matches the stored hash."""
    try:
        parts = stored.split("$")
        if len(parts) != 4 or parts[0] != "pbkdf2_sha256":
            return False
        _, iters, b64_salt, b64_hash = parts
        iters = int(iters)
        salt = base64.b64decode(b64_salt)
        expected = base64.b64decode(b64_hash)
        h = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iters,
            dklen=len(expected),
        )
        return h == expected
    except Exception:
        return False
