POS SYSTEM - README

WHAT IS THIS?
A simple Point of Sale system that runs in command line. Add products with prices, view your cart, and see the total.

HOW TO RUN IT

Windows:
1. Open Command Prompt
2. Go to the folder with point_of_sale.py
3. Type: python point_of_sale.py

Mac/Linux:
1. Open Terminal
2. Go to the folder with point_of_sale.py
3. Type: python3 point_of_sale.py

HOW TO USE IT

1. Choose an option from the menu (1-5)
2. Add Item - Enter product name and price
3. Remove Item - View cart and select item number to remove
4. View Cart - See all items and total price
5. Clear Cart - Empty the entire cart
6. Exit - Close the program

EXAMPLE

Choose option (1-5): 1
Enter product name: Cheese
Enter price: 50
Cheese added to cart - R50.00

Choose option (1-5): 1
Enter product name: Milk
Enter price: 30
Milk added to cart - R30.00

Choose option (1-5): 3

Cheese               R 50.00
Milk                 R 30.00
------------------------------
TOTAL                R 80.00

EXAMPLE

Choose option (1-5): 1
Enter product name: Cheese
Enter price: 50
Cheese added to cart - R50.00

Choose option (1-5): 1
Enter product name: Milk
Enter price: 30
Milk added to cart - R30.00

Choose option (1-5): 3

========================================
CART ITEMS
========================================
1. Cheese               R 50.00
2. Milk                R 30.00
========================================
TOTAL                  R 80.00
========================================