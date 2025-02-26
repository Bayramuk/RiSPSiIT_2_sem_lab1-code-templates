# Ошибки:
# 1. Пароль в коде.
# 2. Нет шифрования соединения.
# 3. Нет обработки ошибок.
import smtplib
def send_email(to, message):
    server = smtplib.SMTP("smtp.gmail.com")
    server.login("admin@company.com", "qwerty123")
    server.sendmail("noreply@company.com", to, message)