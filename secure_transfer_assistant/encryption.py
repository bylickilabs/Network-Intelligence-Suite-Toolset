
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import secrets
import string

def generate_key():
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(32))

def encrypt_file(input_path, output_path, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        f_out.write(iv)
        f_out.write(encryptor.update(f_in.read()) + encryptor.finalize())

def decrypt_file(input_path, output_path, key):
    with open(input_path, "rb") as f:
        iv = f.read(16)
        cipher = Cipher(algorithms.AES(key.encode()), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        data = decryptor.update(f.read()) + decryptor.finalize()
        with open(output_path, "wb") as out:
            out.write(data)
