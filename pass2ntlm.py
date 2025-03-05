#!/usr/bin/env python3

import hashlib
import sys

def create_ntlm_hash(password):
    # Encode the password in UTF-16LE
    encoded_password = password.encode('utf-16le')
    
    # Create the MD4 hash of the encoded password
    ntlm_hash = hashlib.new('md4', encoded_password).digest()
    
    # Return the hash as a hexadecimal string
    return ntlm_hash.hex()

def main():
    # Check if the script was run with the correct argument
    if len(sys.argv) != 2:
        print("Usage: ntlm_hash.py <password>")
        sys.exit(1)

    # The password is the first argument
    password = sys.argv[1]

    # Generate the NTLM hash
    ntlm_hash = create_ntlm_hash(password)

    # Print the result
    print(f"NTLM hash for '{password}': {ntlm_hash}")

if __name__ == "__main__":
    main()
