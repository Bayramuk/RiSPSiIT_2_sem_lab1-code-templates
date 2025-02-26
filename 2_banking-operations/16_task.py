# Ошибки:
# 1. Уязвимость к Path Traversal.
# 2. Нет обработки бинарных файлов (PDF читается как текст).
# 3. Пароль в коде для дешифровки.
def parse_pdf(filename):
    with open(filename, "r") as file:
        return file.read()

def decrypt(data):
    return data.replace("1234", "")  # Пароль в коде