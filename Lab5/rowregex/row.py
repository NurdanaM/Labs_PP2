import re
import json

file_path = "/Users/nurdanam/Desktop/all_labs_pp2/Lab5/rowregex/row.txt"
output_file = "/Users/nurdanam/Desktop/all_labs_pp2/Lab5/rowregex/row.json"

with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

def safe_search(pattern, text, group=1, default=""):
    match = re.search(pattern, text)
    return match.group(group) if match else default

company_info = {
    "name": safe_search(r"Филиал\s+(.+)", text),
    "BIN": safe_search(r"БИН\s+(\d+)", text),
    "VAT": {
        "series": safe_search(r"НДС Серия\s+(\d+)", text),
        "number": safe_search(r"№\s+(\d+)", text)
    }
}

cash_register_info = {
    "number": safe_search(r"Касса\s+([\d-]+)", text),
    "shift": int(safe_search(r"Смена\s+(\d+)", text, default="0")),
    "receipt_number": int(safe_search(r"Порядковый номер чека №\s*(\d+)", text, default="0")),
    "fiscal_receipt_number": safe_search(r"Чек №\s*(\d+)", text),
    "cashier": safe_search(r"Кассир\s+(.+)", text)
}

item_pattern = re.compile(r"(\d+)\.\n(.+?)\n([\d,]+) x ([\d,]+)\n([\d,]+)", re.DOTALL)
items = []

for match in item_pattern.findall(text):
    items.append({
        "name": match[1].strip(),
        "quantity": float(match[2].replace(",", ".")),
        "unit_price": float(match[3].replace(",", ".")),
        "total_price": float(match[4].replace(",", "."))
    })

payment_info = {
    "method": "Банковская карта",
    "amount": float(safe_search(r"Банковская карта:\s*([\d,]+)", text, default="0").replace(",", "."))
}

total_info = {
    "amount": float(safe_search(r"ИТОГО:\s*([\d,]+)", text, default="0").replace(",", ".")),
    "VAT_12_percent": float(safe_search(r"в т.ч. НДС 12%:\s*([\d,]+)", text, default="0").replace(",", "."))
}

fiscal_info = {
    "fiscal_sign": safe_search(r"Фискальный признак:\s*(\d+)", text),
    "time": safe_search(r"Время:\s*([\d.:\s]+)", text),
    "location": safe_search(r"г\.\s*(.+?),", text),
    "operator": safe_search(r"Оператор фискальных данных:\s*(.+?)Для", text).strip(),
    "verification_site": "consumer.oofd.kz"
}

fiscal_device = {
    "INK_OFD": safe_search(r"ИНК ОФД:\s*(\d+)", text),
    "KKM_KGD_code": safe_search(r"Код ККМ КГД \(РНМ\):\s*(\d+)", text),
    "ZNM": safe_search(r"ЗНМ:\s*(\w+)", text),
    "system": "WEBKASSA.KZ"
}

parsed_data = {
    "company": company_info,
    "cash_register": cash_register_info,
    "items": items,
    "payment": payment_info,
    "total": total_info,
    "fiscal_info": fiscal_info,
    "fiscal_device": fiscal_device
}

with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(parsed_data, json_file, indent=4, ensure_ascii=False)

print(f"JSON-файл создан: {output_file}")