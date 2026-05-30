def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    card_str = str(card_number)  # Преобразуем число в строку
    masked_number = []

    for i in range(len(card_str)):  # i — это индекс (позиция)
        if 6 <= i <= 11:
            masked_number.append("*")
        else:
            masked_number.append(card_str[i])

    # Превращаем список в строку
    masked_str = "".join(masked_number)

    # Добавляем пробелы после каждого 4-го символа
    return f"{masked_str[:4]} {masked_str[4:8]} {masked_str[8:12]} {masked_str[12:16]}"


# print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    account_str = str(account_number)  # "73654108430135874305"
    last_four = account_str[-4:]  # "4305" (последние 4 символа)
    masked_account = "**" + last_four  # "**4305"
    return masked_account


# print(get_mask_account(73654108430135874305))
