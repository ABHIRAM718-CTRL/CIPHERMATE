import os
import base64
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}


def aes_encrypt(plain_text):
    key = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    padded_text = plain_text.ljust(16)
    encrypted_bytes = encryptor.update(
        padded_text.encode()) + encryptor.finalize()
    return base64.b64encode(encrypted_bytes).decode(), base64.b64encode(
        key).decode()


def aes_decrypt(encrypted_text, key):
    key = base64.b64decode(key)
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    decrypted_bytes = decryptor.update(
        base64.b64decode(encrypted_text)) + decryptor.finalize()
    return decrypted_bytes.decode().strip()


def morse_encrypt(text):
    return ' '.join(MORSE_CODE_DICT[char] for char in text.upper())


def morse_decrypt(morse_text):
    morse_dict_reversed = {
        value: key
        for key, value in MORSE_CODE_DICT.items()
    }
    return ''.join(morse_dict_reversed[code] for code in morse_text.split())


def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 +
                                  shift_base)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    while True:
        print("\nWelcome to CipherMate!")
        print("Please choose an option:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        action = input("Enter your choice: ")

        if action == '1':
            print("\nChoose an encryption method:")
            print("1. Cryptography (AES, Caesar Cipher)")
            print("2. Morse Code")
            method = input("Enter your choice: ")

            if method == '1':
                print("\nChoose a cryptographic method:")
                print("1. AES Encryption")
                print("2. Caesar Cipher Encryption")
                crypto_choice = input("Enter your choice: ")

                if crypto_choice == '1':
                    text = input("Enter text to encrypt: ")
                    encrypted, key = aes_encrypt(text)
                    print(f"\nEncrypted Message: {encrypted}")
                    print(f"AES Key: {key}")
                elif crypto_choice == '2':
                    text = input("Enter text to encrypt: ")
                    try:
                        shift = int(input("Enter shift key (0–25): "))
                        if 0 <= shift <= 25:
                            encrypted_text = caesar_encrypt(text, shift)
                            print(
                                f"\nEncrypted Caesar Cipher: {encrypted_text}")
                        else:
                            print(
                                "Invalid shift key. Please enter a number between 0 and 25."
                            )
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                else:
                    print("Invalid cryptographic choice. Please try again.")

            elif method == '2':
                text = input("Enter text to convert into Morse Code: ")
                print(f"\nEncrypted Morse Code: {morse_encrypt(text)}")
            else:
                print("Invalid encryption method. Please try again.")

        elif action == '2':
            print("\nChoose a decryption method:")
            print("1. Cryptography (AES, Caesar Cipher)")
            print("2. Morse Code")
            method = input("Enter your choice: ")

            if method == '1':
                print("\nChoose a cryptographic method:")
                print("1. AES Decryption")
                print("2. Caesar Cipher Decryption")
                crypto_choice = input("Enter your choice: ")

                if crypto_choice == '1':
                    encrypted_text = input("Enter encrypted AES text: ")
                    key = input("Enter the AES key: ")
                    try:
                        print(
                            f"\nDecrypted Message: {aes_decrypt(encrypted_text, key)}"
                        )
                    except Exception as e:
                        print(f"Error during decryption: {e}")
                elif crypto_choice == '2':
                    encrypted_text = input(
                        "Enter encrypted Caesar Cipher text: ")
                    try:
                        shift = int(input("Enter shift key (0–25): "))
                        if 0 <= shift <= 25:
                            print(
                                f"\nDecrypted Caesar Cipher: {caesar_decrypt(encrypted_text, shift)}"
                            )
                        else:
                            print(
                                "Invalid shift key. Please enter a number between 0 and 25."
                            )
                    except ValueError:
                        print("Invalid input. Please enter a valid integer.")
                else:
                    print("Invalid cryptographic choice. Please try again.")

            elif method == '2':
                morse_text = input("Enter Morse Code to decrypt: ")
                try:
                    print(f"\nDecrypted Text: {morse_decrypt(morse_text)}")
                except KeyError:
                    print("Invalid Morse Code input. Please check the format.")
            else:
                print("Invalid decryption method. Please try again.")

        elif action == '3':
            print("Exiting CipherMate...")
            print("Current Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
            break
        else:
            print("Invalid main menu choice. Please try again.")


if __name__ == "__main__":
    main()
