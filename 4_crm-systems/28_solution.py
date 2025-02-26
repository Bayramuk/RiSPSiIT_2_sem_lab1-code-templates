"""
Модуль для экспорта данных в XML для 1С.
"""
import xml.etree.ElementTree as ET

def export_to_1c(data: list) -> None:
    """
    Экспортирует данные в XML для 1С.

    Args:
        data (list): Список данных для экспорта.

    Raises:
        ValueError: Если данные пусты.
    """
    if not data:
        raise ValueError("Данные для экспорта пусты!")
    root = ET.Element("root")
    for item in data:
        ET.SubElement(root, "item").text = str(item)
    tree = ET.ElementTree(root)
    tree.write("export.xml", encoding="utf-8", xml_declaration=True)