import sqlite3
import hashlib
import base64
from utils import log_event, validate_password

DB = "data/users.db"

# -------------------------
# HASHING FUNCTION
# -------------------------
def hash_string(text):
    hashed = hashlib.sha256(text.encode()).hexdigest()
    return hashed

# -------------------------
# REGISTER USER
# -------------------------
def register_user():
    print("\n=== User Registration ===")
    username = input("Enter username: ")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    # CHECK IF USER ALREADY EXISTS
    cursor.execute("SELECT username FROM users WHERE username=?", (username,))
    existing = cursor.fetchone()
    if existing:
        print("\n❌ ERROR: Username already exists! Choose a different username.")
        conn.close()
        return

    password = input("Enter password: ")
    role = input("Enter role (user/admin): ").lower()

    if not validate_password(password):
        print("❌ Weak password! Must contain uppercase, lowercase, number, and special characters.")
        conn.close()
        return

    hashed = hash_string(password)

    cursor.execute(
        "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
        (username, hashed, role)
    )
    conn.commit()
    conn.close()

    log_event(f"New user registered: {username} ({role})")
    print("✅ Registration successful!")


# -------------------------
# LOGIN USER
# -------------------------
def login_user():
    print("\n=== User Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT password, role FROM users WHERE username=?", (username,))
    result = cursor.fetchone()

    if not result:
        print("❌ User not found.")
        conn.close()
        return None, None

    stored_hash, role = result
    input_hash = hash_string(password)

    if input_hash == stored_hash:
        print("✅ Login successful!")
        log_event(f"User logged in: {username}")
        conn.close()
        return username, role
    else:
        print("❌ Incorrect password.")
        log_event(f"Failed login attempt for: {username}")
        conn.close()
        return None, None
