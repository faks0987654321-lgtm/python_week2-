

# Import the function that we want to test
from food_order import calculate_total


# Test if 10 * 2 gives 20
def test_order_20():
    assert calculate_total(10, 2) == 20


# Test if 10 * 3 gives 30
def test_order_30():
    assert calculate_total(10, 3) == 30


# Test if 50 * 2 gives 100
def test_order_100():
    assert calculate_total(50, 2) == 100


# Test if 5 * 2 gives 10
def test_order_10():
    assert calculate_total(5, 2) == 10


# Test invalid price
# Price cannot be 0 or less
def test_invalid_price():
    assert calculate_total(0, 2) == "invalid price"


# Test invalid quantity
# Quantity cannot be 0 or less
def test_invalid_quantity():
    assert calculate_total(10, 0) == "invalid quantity"