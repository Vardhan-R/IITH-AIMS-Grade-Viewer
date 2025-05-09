from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def checkPassword(password: str) -> bool:
    encoded_password = password.encode()
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=b"0123456789abcdef",
        iterations=480_000,
    )
    key = urlsafe_b64encode(kdf.derive(encoded_password))
    return key == b"UY1Tooh2llCyd8CIBTkokTNxctVxgvvDS9bdtxjyL1Y="
