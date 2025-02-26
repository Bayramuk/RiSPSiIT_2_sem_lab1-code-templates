"""
Модуль для парсинга банковских выписок в формате PDF.
"""
from pathlib import Path
import PyPDF2

def parse_pdf(filepath: str) -> str:
    """
    Парсит PDF-выписку.

    Args:
        filepath (str): Путь к файлу.

    Returns:
        str: Текст выписки.

    Raises:
        ValueError: Если путь недопустим.
        FileNotFoundError: Если файл не найден.
    """
    if not Path(filepath).resolve().match("/bank_statements/*"):
        raise ValueError("Недопустимый путь к файлу!")
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        return reader.pages[0].extract_text()