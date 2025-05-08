from cryptography.fernet import Fernet

def decrypt_file(file_path: str, key: bytes | str) -> bytes:
	with open(file_path, 'rb') as fp:
		encrypted_data = fp.read()
	fernet = Fernet(key)
	return fernet.decrypt(encrypted_data)
