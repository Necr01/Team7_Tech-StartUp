import sqlite3
import os

DB_PATH = "data/users.db"

def view_users():
    if not os.path.exists(DB_PATH):
        print("❌ Database not found. Run the system first to create 'users.db'.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT username, password, role FROM users")
        users = cursor.fetchall()

        if not users:
            print("⚠️ No users found in the database.")
            return

        print("\n=== Stored Users & Hashed Passwords ===")
        for user in users:
            username, password_hash, role = user
            print(f"\nUsername: {username}")
            print(f"Role: {role}")
            print(f"Hashed Password: {password_hash}")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    view_users()

