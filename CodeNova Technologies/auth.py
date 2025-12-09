import sqlite3
from utils import hash_string, validate_password, timestamp, log_event

DB = "data/users.db"

def register_user():
    print("\n=== User Registration ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (user/admin): ").lower()

    if not validate_password(password):
        print("Weak password! Must contain uppercase, lowercase, number, and special characters.")
        return

    hashed = hash_string(password)

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   (username, hashed, role))
    conn.commit()
    conn.close()

    log_event(f"New user registered: {username} ({role})")
    print("Registration successful!")

def login_user():
    print("\n=== User Login ===")
    username = input("Username: ")
    password = input("Password: ")

    hashed = hash_string(password)

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    cursor.execute("SELECT username, role FROM users WHERE username=? AND password=?", (username, hashed))
    result = cursor.fetchone()
    conn.close()

    if result:
        log_event(f"User logged in: {username}")
        return {"username": result[0], "role": result[1]}
    else:
        print("Invalid credentials!")
        log_event(f"FAILED login attempt for user: {username}")
        return None
