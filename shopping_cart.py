"""
A simple shopping cart program to calculate and display the total price.
"""

def calculate_total(cart):
    """
    Calculates the total price of all items in the shopping cart.
    """
    total = 0
    for cart_item in cart:
        total += cart_item['price']
    return total

def display_total(total):
    """
    Displays the calculated total price in a user-friendly format.
    """
    print("Total price: " + str(total))

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': 8.49}
]

for item in CART:
    print(f"Item: {item['name']} - Price: ${item['price']}")

shopping_cart_total = calculate_total(CART)
display_total(shopping_cart_total)
