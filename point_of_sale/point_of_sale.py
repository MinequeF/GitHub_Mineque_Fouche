# Point of Sale (POS) System
# This program manages a simple store with products and prices
# Users can add items to a cart and see the total cost

# List to store all items in the cart
cart = []

# Function to add an item to the cart
def add_item(product_name, price):
    # Add the product and price as a dictionary to the cart list
    item = {
        'name': product_name,
        'price': price
    }
    cart.append(item)
    print(f"{product_name} added to cart - R{price:.2f}")

# Function to remove an item from the cart
def remove_item(index):
    # Check if the index is valid
    if 0 <= index < len(cart):
        removed_item = cart.pop(index)
        print(f"{removed_item['name']} removed from cart")
    else:
        print("Invalid item number")

# Function to display all items and total
def display_cart():
    # Check if cart is empty
    if len(cart) == 0:
        print("\nCart is empty")
        return
    
    print("\n")
    
    # Loop through each item in the cart
    total = 0
    for item in cart:
        print(f"{item['name']:<20} R{item['price']:>7.2f}")
        total += item['price']
    
    # Display the total with separator line
    print("-" * 30)
    print(f"{'TOTAL':<20} R{total:>7.2f}\n")
    
    return total

# Function to clear the cart
def clear_cart():
    # Empty the cart list
    cart.clear()
    print("Cart cleared")

# Main program function
def main():
    # Sentinel variable to control the main loop
    running = True
    
    print("\n" + "=" * 40)
    print("WELCOME TO POS SYSTEM")
    print("=" * 40)
    
    # Main loop - continues until user exits
    while running:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Clear cart")
        print("5. Exit")
        
        # Get user choice
        choice = input("\nChoose option (1-5): ")
        
        if choice == '1':
            # Add item option
            try:
                product = input("Enter product name: ")
                price = float(input("Enter price: R"))
                add_item(product, price)
            except ValueError:
                print("Invalid price. Please enter a number.")
        
        elif choice == '2':
            # Remove item option
            display_cart()
            try:
                item_num = int(input("Enter item number to remove: "))
                remove_item(item_num - 1)
            except ValueError:
                print("Invalid number")
        
        elif choice == '3':
            # View cart option
            display_cart()
        
        elif choice == '4':
            # Clear cart option
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                clear_cart()
        
        elif choice == '5':
            # Exit option
            confirm = input("Are you sure you want to exit? (y/n): ")
            if confirm.lower() == 'y':
                # Set sentinel to False to exit the loop
                running = False
                print("\nThank you for using POS System. Goodbye!\n")
        
        else:
            print("Invalid option. Please choose 1-5")

# Run the program
if __name__ == "__main__":
    main()