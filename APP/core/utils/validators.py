import re 
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PHONE_PATTERN = r'^01[0125]\d{8}$'
VALID_ROLES = {'buyer', 'seller', 'admin'}

def is_valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_PATTERN, email))

def is_valid_phone(phone: str) -> bool:
    return bool(re.match(PHONE_PATTERN, phone))

def is_valid_role(role: str) -> bool:
    if role not in VALID_ROLES:
        return False
    return True