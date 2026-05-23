import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    ('7000792289606361', '7000 79** **** 6361'),
    ('1234567890123456', '1234 56** **** 3456'),
    ('4111111111111111', '4111 11** **** 1111'),
   ])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

@pytest.mark.parametrize('value, expected', [
    ('73654108430135874305', '**4305'),
    ('73654308430135574215', '**4215'),
    ('73654108527235873205', '**3205'),
   ])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected

