

# This function calculates the total payment for a food order
def calculate_total(price, quantity):

    # Check if the price is invalid
    # Price should be more than 0
    if price <= 0:
        return "invalid price"

    # Check if the quantity is invalid
    # Quantity should be more than 0
    if quantity <= 0:
        return "invalid quantity"

    # Calculate the total payment
    total = price * quantity

    # Return the final total
    return total