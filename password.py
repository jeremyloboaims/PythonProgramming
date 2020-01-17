import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

password_provided = input("Enter your password: ")
password = password_provided.encode()
salt = b'\xe2\x0e\xf6V\x13\x0ep\xdd<\x065D\xac5FN'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

print(key)

file = open("key.key", "wb")
file.write(key)
file.close()
file = open('key.key', 'rb')
f = Fernet(key)
encrypted = f.encrypt(password)
print(encrypted)
decrypted = f.decrypt(encrypted)
print(decrypted.decode())


