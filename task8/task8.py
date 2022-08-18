from cryptography.fernet import Fernet
key = Fernet.generate_key() 
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"this text will be encrypted using python")
print(encoded_text , "\n")
decoded_text = cipher_suite.decrypt(encoded_text)
print(decoded_text, "\n")

