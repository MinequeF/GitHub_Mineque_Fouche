# Calculator Program
# A simple command-line calculator that performs basic arithmetic operations
# The program loops until the user chooses to exit

# Addition function
def add(num1, num2):
    return num1 + num2

# Subtraction function
def subtract(num1, num2):
    return num1 - num2

# Multiplication function
def multiply(num1, num2):
    return num1 * num2

# Division function
def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

# Function to clear the screen
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function that controls the program loop
def main():
    # Sentinel variable - controls whether the loop continues
    running = True
    
    print("\nWelcome to the Calculator!")
    print("=" * 40)
    
    # Main loop - continues until running is False
    while running:
        try:
            # Get first number from user
            num1 = float(input("\nEnter first number: "))
            
            # Get second number from user
            num2 = float(input("Enter second number: "))
            
            # Get the operation the user wants to do
            operation = input("Choose operation (+, -, *, /): ")
            
            # Perform the correct operation based on what user chose
            if operation == '+':
                result = add(num1, num2)
                print(f"\nResult: {num1} + {num2} = {result}")
            
            elif operation == '-':
                result = subtract(num1, num2)
                print(f"\nResult: {num1} - {num2} = {result}")
            
            elif operation == '*':
                result = multiply(num1, num2)
                print(f"\nResult: {num1} * {num2} = {result}")
            
            elif operation == '/':
                result = divide(num1, num2)
                if isinstance(result, str):  # This is an error message
                    print(f"\n{result}")
                else:
                    print(f"\nResult: {num1} / {num2} = {result}")
            
            elif operation == 'c' or operation == 'C':
                # User wants to clear the screen
                clear_screen()
                print("Welcome to the Calculator!")
                print("=" * 40)
                continue
            
            else:
                # Invalid operation
                print("\nError: Please choose '+', '-', '*', or '/'")
                continue
            
            # Ask user if they want to continue
            choice = input("\nDo another calculation? (y/n): ").lower()
            
            if choice == 'n':
                # User wants to stop - set sentinel to False
                running = False
                print("\nThanks for using the calculator. Goodbye!\n")
            
            elif choice == 'y':
                # User wants to continue - loop will run again
                continue
            
            else:
                # Invalid answer
                print("Invalid choice. Continuing...")
        
        except ValueError:
            # User did not enter a valid number
            print("\nError: Please enter valid numbers.")

# Run the program
if __name__ == "__main__":
    main()