# Ошибки:
# 1. Нет обработки пустых данных.
# 2. Пароль в коде (хотя здесь не используется, но предполагается).
# 3. Открытый доступ к файлам без проверки.
def generate_tax_report(data):
    with open("report.csv", "w") as file:
        file.write("User;Income;Tax\n")
        for row in data:
            file.write(f"{row[0]};{row[1]};{row[1]*0.13}\n")