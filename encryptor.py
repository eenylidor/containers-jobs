import argparse
import os
import base64
import hashlib
import sys

def derive_key(password: str, salt: bytes) -> bytes:
    """Derive a 32-byte key using PBKDF2."""
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def xor_bytes(data: bytes, key: bytes) -> bytes:
    """Perform XOR operation between data and a repeating key."""
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def encrypt_file(filepath: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    
    with open(filepath, 'rb') as f:
        plaintext = f.read()
    
    ciphertext = xprint_xor(plaintext, key)
    
    # Output format: [salt (16 bytes)][ciphertext]
    # We encode in base64 for easy handling of text files/binary data
    encoded_data = base64.b64encode(salt + ciphertext)
    
    with open(filepath + ".enc", 'wb') as f:
        f.write(encoded_data)
    print(f"File encrypted successfully: {filepath}.enc")

def decrypt_file(filepath: str, password: str):
    with open(filepath, 'rb') as f:
        encoded_data = f.read()
    
    raw_data = base64.b64decode(encoded_data)
    if len(raw_data) < 16:
        print("Error: Encrypted file is too small or corrupted.")
        return

    salt = raw_data[:16]
    ciphertext = raw_data[16:]
    
    key = derive_key(password, salt)
    plaintext = xprint_xor(ciphertext, key)
    
    output_path = filepath.replace(".enc", ".dec")
    if output_path == filepath:
        output_path += ".dec"

    with open(output_path, 'wb') as f:
        f.write(plaintext)
    print(f"File decrypted successfully: {output_path}")

def xprint_xor(data: bytes, key: bytes) -> bytes:
    # Re-using the logic from xor_bytes to ensure consistency
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Standard-Library File Encryptor")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Action to perform")
    parser.add_argument("file", help="Path to the file")
    parser.add_argument("-p", "--password", required=True, help="Password for encryption/decryption")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    try:
        if args.action == "encrypt":
            encrypt_file(args.file, args.password)
        elif args.action == "decrypt":
            decrypt_file(args.file, args.password)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
