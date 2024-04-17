import pytest

from src.question2 import Orders


@pytest.mark.parametrize("requests, n_max, expected_trips", [
    ([1, 2, 3, 4, 5], 5, 3),
    ([1, 2, 3], 6, 2),
    ([4, 5, 6], 7, 3),
    ([], 5, 0)
])
def test_combine_orders(requests, n_max, expected_trips):
    order_instance = Orders()
    assert order_instance.combine_orders(requests, n_max) == expected_trips
