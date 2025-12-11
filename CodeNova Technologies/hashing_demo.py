# hashing_demo.py
import hashlib
import base64

print("=== SIMPLE HASHING DEMO ===")
text = input("Enter text to hash: ")

# SHA-256 hash
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

# Base64 encoding
b64_encoded = base64.b64encode(text.encode()).decode()

print("\n--- RESULTS ---")
print("Original Text: ", text)
print("SHA-256 Hash: ", sha256_hash)
print("Base64 Encoded: ", b64_encoded)

print("\nNotes:")
print("- Hashing (SHA-256) is ONE-WAY. You cannot reverse it.")
print("- Base64 is reversible. It is NOT encryption.")
