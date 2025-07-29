# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price  # No discount applied if less than 20%

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Use the function to calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Display result
if discount_percentage >= 20:
    print(f"Final price after {discount_percentage}% discount: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")

