import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_another_format():
    assert get_date("2025-12-25T10:30:00.000000") == "25.12.2025"


def test_mask_account_card_empty_str():
    assert mask_account_card("") == "Ошибка: пустая строка"


def test_mask_account_card_no_digits():
    assert mask_account_card("Maestro") == "Ошибка: не найдено цифр"


def test_mask_account_card_no_letters():
    assert mask_account_card("1596837868705199") == "Ошибка: не найдено букв"


@pytest.mark.parametrize(
    "invalid_input, expected_type",
    [
        (1596837868705199, "int"),
        (12345.6789, "float"),
        (["Visa", "1234"], "list"),
        ({"card": "1234"}, "dict"),
        (True, "bool"),
    ],
)
def test_mask_account_card_type_error(invalid_input, expected_type):
    with pytest.raises(TypeError) as exc_info:
        mask_account_card(invalid_input)

    expected_message = f"Ожидалась строка, получен {expected_type}"
    assert str(exc_info.value) == expected_message
