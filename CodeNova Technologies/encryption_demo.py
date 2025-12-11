# encryption_demo.py
import base64

print("=== SIMPLE ENCRYPTION / ENCODING DEMO ===")

text = input("Enter text to encode (Base64): ")

# Encode to Base64
encoded = base64.b64encode(text.encode()).decode()

# Decode back to original text
decoded = base64.b64decode(encoded.encode()).decode()

print("\n--- RESULTS ---")
print("Original Text: ", text)
print("Base64 Encoded: ", encoded)
print("Decoded Back: ", decoded)

print("\nNotes:")
print("- Base64 is NOT encryption.")
print("- It only encodes data for safe storage or transfer.")
print("- It can ALWAYS be reversed back to original form.")
