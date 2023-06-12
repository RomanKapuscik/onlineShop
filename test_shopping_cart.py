import pytest
from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart()


def test_can_add_item_to_cart(cart):
    cart.add('mydlo')
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add('mydlo')
    assert 'mydlo' in cart.get_items()


def test_when_add_more_than_max_size_should_fail(cart):
    for _ in range(5):
        cart.add('mydlo')
    with pytest.raises(OverflowError):
        cart.add('mydlo')


def test_get_total_price(cart):
    cart.add('mydlo')
    cart.add('powidlo')
    assert cart.get_total_price() == 3.0

