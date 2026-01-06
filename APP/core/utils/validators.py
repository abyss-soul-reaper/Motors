import re 
EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
PHONE_PATTERN = r'^01[0125]\d{8}$'

def is_valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_PATTERN, email))

def is_valid_phone(phone: str) -> bool:
    return bool(re.match(PHONE_PATTERN, phone))