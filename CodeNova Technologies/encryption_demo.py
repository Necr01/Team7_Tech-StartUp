import base64
from utils import hash_string

def encryption_demo():
    text = input("\nEnter text to encrypt: ")

    print("\n--- Encryption Demo ---")
    print("SHA-256 Hash:", hash_string(text))
    print("Base64 Encode:", base64.b64encode(text.encode()).decode())
