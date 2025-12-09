import json
import hashlib
import datetime
import os

def hash_string(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()

def read_json(filepath: str):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)

def write_json(filepath: str, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_password(password: str) -> bool:
    if len(password) < 8: return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{};:,.<>?" for c in password)
    return has_upper and has_lower and has_digit and has_special

def log_event(message: str, log_file="system.log"):
    with open(log_file, "a") as f:
        f.write(f"[{timestamp()}] {message}\n")
