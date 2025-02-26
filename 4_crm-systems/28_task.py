# Ошибки:
# 1. Неправильный XML-формат (ручная сборка строки).
# 2. Нет шифрования данных.
# 3. Уязвимость к XML-инъекциям.
def export_to_1c(data):
    xml = "<root>"
    for item in data:
        xml += f"<item>{item}</item>"
    xml += "</root>"
    with open("export.xml", "w") as file:
        file.write(xml)