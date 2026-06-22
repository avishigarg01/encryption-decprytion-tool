# fernet_cipher.py
# This file has the secure encryption method using the "cryptography" library.
# It uses something called Fernet, which does strong encryption (AES) for us.
#
# How it works:
#  - First we create a secret "key" (a long random password).
#  - We use that key to encrypt the data.
#  - We need the SAME key again to decrypt it.
# If you lose the key, you cannot get the data back!

from cryptography.fernet import Fernet


# This makes a brand new secret key and saves it in a file called secret.key
def generate_key():
    key = Fernet.generate_key()  # this is the random secret key

    # save the key into a file so we can use it again later
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("A new secret key was created and saved as 'secret.key'")
    return key


# This reads the key back from the secret.key file
def load_key():
    return open("secret.key", "rb").read()


# This encrypts a piece of text using the key
def encrypt_text(text, key):
    f = Fernet(key)
    # Fernet works on bytes, so we turn the text into bytes with .encode()
    encrypted = f.encrypt(text.encode())
    return encrypted  # this comes back as scrambled bytes


# This decrypts the text using the same key
def decrypt_text(token, key):
    f = Fernet(key)
    decrypted = f.decrypt(token)
    # turn the bytes back into normal readable text with .decode()
    return decrypted.decode()


# This encrypts a whole file and saves it as a new file
def encrypt_file(input_file, output_file, key):
    try:
        f = Fernet(key)

        # read the original file (rb = read in bytes mode)
        with open(input_file, "rb") as file:
            data = file.read()

        # encrypt all the data
        encrypted_data = f.encrypt(data)

        # save the encrypted data into the new file
        with open(output_file, "wb") as file:
            file.write(encrypted_data)

        print("File encrypted successfully! Saved as:", output_file)

    except FileNotFoundError:
        print("Sorry, the file was not found:", input_file)


# This decrypts a whole file using the same key
def decrypt_file(input_file, output_file, key):
    try:
        f = Fernet(key)

        with open(input_file, "rb") as file:
            data = file.read()

        # decrypt the data back to normal
        decrypted_data = f.decrypt(data)

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully! Saved as:", output_file)

    except FileNotFoundError:
        print("Sorry, the file was not found:", input_file)


# This part lets us test this file on its own.
if __name__ == "__main__":
    # make a key for testing
    my_key = generate_key()

    message = "This is a secret message"

    locked = encrypt_text(message, my_key)
    unlocked = decrypt_text(locked, my_key)

    print("Original :", message)
    print("Encrypted:", locked)
    print("Decrypted:", unlocked)
