import hashlib
import base64
import sqlite3
import os

# --- Setup SQLite database ---
DATA_DIR = "data"
DB_PATH = os.path.join(DATA_DIR, "users.db")
os.makedirs(DATA_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
''')
conn.commit()


# --- Functions ---

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def register_user():
    print("\n=== User Registration ===")
    username = input("Enter username: ")
    password = input("Enter password (min 8 chars, upper/lower/number/special): ")

    # Password strength check
    if (len(password) < 8 or
        not any(c.isupper() for c in password) or
        not any(c.islower() for c in password) or
        not any(c.isdigit() for c in password) or
        not any(c in '!@#$%^&*()-_=+[]{};:,.<>?' for c in password)):
        print("❌ Password does not meet strength requirements.")
        return

    hashed_pw = sha256_hash(password)
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        conn.commit()
        print("✅ User registered successfully!")
        print(f"SHA-256 Hash Stored in DB: {hashed_pw}")
        print(f"Base64 Encoded Password: {base64_encode(password)}")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")


def login_user():
    print("\n=== User Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_pw = sha256_hash(password)

    cur.execute("SELECT username FROM users WHERE username=? AND password=?", (username, hashed_pw))
    row = cur.fetchone()
    if row:
        print(f"✅ Login successful! Welcome, {username}")
        print(f"SHA-256 of your input password: {hashed_pw}")
        print(f"Base64 encoded input: {base64_encode(password)}")
    else:
        print("❌ Invalid username or password.")


def main():
    print("=== CodeNova Crypto Demo ===")
    while True:
        print("\nSelect option:")
        print("[1] Register User")
        print("[2] Login User")
        print("[3] Exit")
        choice = input("Choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting demo. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
