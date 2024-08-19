def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if the discount is 20% or higher."""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: R"))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price < original_price:
        print(f"The final price after applying a {discount_percentage}% discount is: R{final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: R{original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
