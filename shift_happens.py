#!/usr/bin/env python3

import sys

def caesar_cipher(text: str, shift: int) -> str:
    """Apply Caesar cipher to the input text using the given shift.
    
    Non-alphabetical characters are left unchanged.
    """
    result = []
    for char in text:
        if char.isalpha():
            # Determine the starting ASCII value depending on case.
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character, wrapping around the alphabet.
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)
    return ''.join(result)

def main():
    if len(sys.argv) != 5:
        print("Usage: python shift_happens.py <encrypt|decrypt> <shift_value> <input_file> <output_file>")
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    try:
        shift = int(sys.argv[2])
    except ValueError:
        print("Error: shift must be an integer")
        sys.exit(1)
    
    input_file = sys.argv[3]
    output_file = sys.argv[4]
    
    # For decryption, reverse the shift.
    if mode == "decrypt":
        shift = -shift
    elif mode != "encrypt":
        print("Error: mode must be 'encrypt' or 'decrypt'")
        sys.exit(1)
    
    # Read the input file (assumed to be text)
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Apply the Caesar cipher transformation.
    transformed_text = caesar_cipher(text, shift)
    
    # Write the result to the output file.
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transformed_text)

if __name__ == "__main__":
    main()

