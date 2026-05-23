from tkinter.messagebox import CANCEL

import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected_data", [
    ("EXECUTED", [{"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
        ]),
    ("CANCELED", [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ])
])
def test_filter_by_state_executed(state, expected_data, operations_data):

    result = filter_by_state(operations_data, state)
    expected = expected_data
    assert result == expected


@pytest.mark.parametrize('descending, expected_order', [
    (
        True,
        [
            {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
            {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        ]
    ),
    (
        False,
        [
            {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        ]
    ),
])
def test_sort_by_date(sample_operations, descending, expected_order):
    result = sort_by_date(sample_operations, descending=descending)
    for i, expected in enumerate(expected_order):
        assert result[i]["id"] == expected["id"]
        assert result[i]["date"] == expected["date"]