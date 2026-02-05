import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations):
    result = filter_by_state(operations)
    assert len(result) == 2
    assert all(op['state'] == 'EXECUTED' for op in result)


@pytest.mark.parametrize(
    'state, expected_len',
    [
        ('EXECUTED', 2),
        ('CANCELED', 1),
        ('UNKNOWN', 0),
    ],
)
def test_filter_by_state_parametrized(operations, state, expected_len):
    result = filter_by_state(operations, state)
    assert len(result) == expected_len


def test_sort_by_date_desc(operations):
    result = sort_by_date(operations)
    dates = [op['date'] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_asc(operations):
    result = sort_by_date(operations, reverse=False)
    dates = [op['date'] for op in result]
    assert dates == sorted(dates)
