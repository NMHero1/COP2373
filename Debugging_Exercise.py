# This program is designed to apply discounts to a list of products and return their information.

def calculate_discount(price, discount_rate):

    # Calculate the discount amount based on the price and discount rate.
    discount_amount = price * discount_rate
    return discount_amount

def apply_discount(price, discount_amount):

    # Apply the discount amount to the original price and return the new price.
    new_price = price - discount_amount
    return new_price

def main():

    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": 500, "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    # Iterate through the table of products
    for product in products:
        price = product["price"]
        discount_rate = product["discount_rate"]

        # Ensure that price and discount rate are numeric
        try:

            # Attempt to convert price and discount_rate to float values
            price = float(price)
            discount_rate = float(discount_rate)

            # Calculate values
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            # Print product information
            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()

        except ValueError:

            # Handle invalid input
            print(f"Error: Price '{price}' or Discount Rate '{discount_rate}' is not a valid number.")

if __name__ == "__main__":
    main()


