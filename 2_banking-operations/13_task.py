# Ошибки:
# 1. Слабый алгоритм хеширования (MD5).
# 2. Нет "соли" для повышения безопасности.
# 3. Хранение паролей в открытом виде.
import hashlib

def verify_signature(user, password, signature):
    stored_hash = "5f4dcc3b5aa765d61d8327deb882cf99"  # md5("password")
    return hashlib.md5(password.encode()).hexdigest() == stored_hash