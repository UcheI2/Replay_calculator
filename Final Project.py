

# Function to safely get a number from the user
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Store previous calculations
history = []

# Main calculator loop
while True:
    # Show menu
    print("\nOptions:")
    print("1. Perform a new calculation")
    print("2. View calculation history")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    # Option 1: New calculation created by user
    if choice == "1":

        while True:
            operator = input("Enter an operator (Add = +, Sub = -, Multiply = *, Division = /): ")
            if operator in ['+', '-', '*', '/']:
                break
            print("Invalid operator. Please enter a valid operator.")

        # Get numbers from user
        num1 = get_number("Enter the 1st number: ")
        num2 = get_number("Enter the 2nd number: ")

        # Perform operation (Ask user to pick)
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero.")
                continue

        # Store and display result
        calculation = f"{num1} {operator} {num2} = {result}"
        print("Your answer is:", result)
        history.append(calculation)

    # Option 2: Show history (Of Previous Caculations)
    elif choice == "2":
        if not history:
            print("No previous calculations.")
        else:
            print("\nCalculation History:")
            for i, calc in enumerate(history, 1):
                print(f"{i}: {calc}")

    # Option 3: Exit (Ends)
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
