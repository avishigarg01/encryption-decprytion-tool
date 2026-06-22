# caesar_cipher.py
# This file has the Caesar Cipher method.
# The Caesar Cipher works by shifting every letter forward in the alphabet
# by a fixed number called the "key" (or shift).
# Example: with a key of 3 -> A becomes D, B becomes E, C becomes F ...
#
# NOTE: The Caesar Cipher is NOT secure. It is only here to learn the idea.


# This function encrypts a piece of text using the Caesar Cipher.
def encrypt_text(text, key):
    result = ""  # we will build the encrypted text here

    # go through each character one by one
    for char in text:

        # only shift the letters (A-Z and a-z), leave other things as they are
        if char.isupper():
            # ord() gives the number of the letter, chr() turns it back to a letter
            # we subtract 65 because 'A' is 65, do the shift, then add 65 again
            # the % 26 makes the letters "wrap around" (so Z goes back to A)
            new_char = chr((ord(char) - 65 + key) % 26 + 65)
            result = result + new_char

        elif char.islower():
            # same idea but 'a' is 97
            new_char = chr((ord(char) - 97 + key) % 26 + 97)
            result = result + new_char

        else:
            # numbers, spaces and symbols stay the same
            result = result + char

    return result


# This function decrypts the text.
# Decrypting is just encrypting with the opposite (negative) shift.
def decrypt_text(text, key):
    return encrypt_text(text, -key)


# This function encrypts a whole file.
# It reads the file, encrypts the text, and saves it to a new file.
def encrypt_file(input_file, output_file, key):
    try:
        # open and read the original file
        with open(input_file, "r") as f:
            data = f.read()

        # encrypt the text we read
        encrypted_data = encrypt_text(data, key)

        # save the encrypted text into the new file
        with open(output_file, "w") as f:
            f.write(encrypted_data)

        print("File encrypted successfully! Saved as:", output_file)

    except FileNotFoundError:
        print("Sorry, the file was not found:", input_file)


# This function decrypts a whole file (same idea, opposite shift).
def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, "r") as f:
            data = f.read()

        decrypted_data = decrypt_text(data, key)

        with open(output_file, "w") as f:
            f.write(decrypted_data)

        print("File decrypted successfully! Saved as:", output_file)

    except FileNotFoundError:
        print("Sorry, the file was not found:", input_file)


# This part lets us quickly test the file on its own.
# It only runs if we run this file directly (not when it is imported).
if __name__ == "__main__":
    message = "Hello World"
    shift = 3

    locked = encrypt_text(message, shift)
    unlocked = decrypt_text(locked, shift)

    print("Original :", message)
    print("Encrypted:", locked)
    print("Decrypted:", unlocked)
