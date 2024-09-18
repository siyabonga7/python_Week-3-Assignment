def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after discount or original price if discount is less than 20%
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
    else:
        final_price = price
    return final_price

def main():
    try:
        # Prompt user for input
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate final price
        final_price = calculate_discount(price, discount_percent)

        # Print the final price
        print(f"Final price after discount: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount.")

if __name__ == "__main__":
    main()
