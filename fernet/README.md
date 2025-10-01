# Fernet Key Demonstration

This script demonstrates the use of Fernet keys for encryption and decryption. It is intended to be used to demonstrate secret detection.

## Description

The `main.py` script provides a simple command-line interface to perform the following actions:

- Generate a new Fernet key and saving it to `secret.key`.
- Encrypt the contents of a file (`sample.txt`).
- Decrypt the contents of a file (`sample.txt`).

## Installation

1.  Clone the repository.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, execute the following command:

```bash
python main.py
```

## How it works

The script uses the `cryptography` library to perform encryption and decryption.

-   `generate_key()`: Creates a new Fernet key.
-   `load_key()`: Reads the key from the `secret.key` file.
-   `encrypt_file()`: Encrypts the specified file using the key.
-   `decrypt_file()`: Decrypts the specified file using the key.
