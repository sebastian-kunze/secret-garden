
from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it into a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Loads the key from the current directory named `secret.key`"""
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    """Given a filename (str) and key (bytes), it encrypts the file and writes it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    """Given a filename (str) and key (bytes), it decrypts the file and writes it"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    # generate a key
    generate_key()
    # load the key
    key = load_key()
    # file to encrypt
    file = "sample.txt"
    # encrypt the file
    encrypt_file(file, key)
    print(f"File {file} encrypted.")
    # decrypt the file
    decrypt_file(file, key)
    print(f"File {file} decrypted.")
