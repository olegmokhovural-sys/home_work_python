from masks import get_mask_account, get_mask_card_number


def init_row_separation(letters_digits: str) -> str:
    if not letters_digits:
        return "Ошибка: пустая строка"

    if not isinstance(letters_digits, str):
        raise TypeError(f"Ожидалась строка, получен {type(letters_digits).__name__}")

    letters = []
    digits = []

    for i in letters_digits:
        if i.isalpha() or i.isspace():
            letters.append(i)
        elif i.isdigit():
            digits.append(i)

    letters_str = "".join(letters).strip()
    digits_str = "".join(digits)

    if not digits_str:
        return "Ошибка: не найдено цифр"
    if not letters_str:
        return "Ошибка: не найдено букв"

    if letters_str == "Счет":
        if len(digits_str) != 20:
            return f"Ошибка: номер счета должен содержать 20 цифр (получено {len(digits_str)})"
        return f"{letters_str} {get_mask_account(digits_str)}"
    else:
        if len(digits_str) != 16:
            if len(digits_str) > 16:
                return f"Ошибка: номер содержит {len(digits_str)} цифр (ожидается 16). Возможно, введены лишние цифры"
            else:
                return f"Ошибка: номер карты содержит {len(digits_str)} цифр (ожидается 16)"
        if len(letters_str) < 2:
            return "Ошибка: название карты слишком короткое"
        return f"{letters_str} {get_mask_card_number(digits_str)}"


# Использование
card_info = input("Введите данные: ")
print(init_row_separation(card_info))


def get_date(date_string: str) -> str:
    """Преобразует ISO дату в формат ДД.ММ.ГГГГ"""
    return f"{date_string[8:10]}.{date_string[5:7]}.{date_string[:4]}"


result = get_date("2024-03-11T02:26:18.671407")
print(f"ДД.ММ.ГГГГ {result}")
