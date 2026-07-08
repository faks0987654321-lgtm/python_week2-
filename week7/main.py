
# Import the calculate_total function from food_order.py
from food_order import calculate_total


# Main function of the program
def main():

    # Ask the user to enter the food price
    # float is used because price can have decimal values
    price = float(input("Price (RM): "))

    # Ask the user to enter the quantity
    # int is used because quantity should be a whole number
    quantity = int(input("Quantity: "))

    # Call calculate_total function and store the result
    total = calculate_total(price, quantity)

    # If the result is text, it means there is an error
    if isinstance(total, str):
        print(total)

    # If the result is a number, print the total payment
    else:
        print(f"Total Payment = RM {total:.2f}")


# This makes sure main() runs only when this file is executed directly
if __name__ == "__main__":
    main()