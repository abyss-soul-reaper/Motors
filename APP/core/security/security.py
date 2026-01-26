import hashlib
HASH_ALGORITHM = "sha256"

def hash_password(password: str) -> str:
    hash_obj = hashlib.new(HASH_ALGORITHM)
    hash_obj.update(password.encode())
    return hash_obj.hexdigest()