"""
Модуль для отправки email-уведомлений.
"""
import smtplib
from email.mime.text import MIMEText
from getpass import getpass

def send_email(to: str, message: str) -> None:
    """
    Отправляет email-уведомление.

    Args:
        to (str): Адрес получателя.
        message (str): Текст сообщения.

    Raises:
        ValueError: Если адрес или сообщение пустые.
        RuntimeError: При ошибке отправки.
    """
    if not to or not message:
        raise ValueError("Адрес и сообщение не могут быть пустыми!")
    password = getpass("Введите пароль: ")
    msg = MIMEText(message)
    msg["Subject"] = "Уведомление"
    msg["From"] = "noreply@company.com"
    msg["To"] = to
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login("admin@company.com", password)
            server.send_message(msg)
    except smtplib.SMTPException as e:
        raise RuntimeError(f"Ошибка отправки: {e}")