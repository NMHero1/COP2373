# This program is designed to analyze a user's expenses and return their highest and lowest expense.

# Import the reduce method
from functools import reduce

# Define function to get user expenses
def get_expenses():

    # Create list to store expenses
    expenses = []

    # Loop to prompt user to enter expenses
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")

        # Stop looping if user enters "done"
        if expense_type.lower() == "done":
            break

        # Try block to prevent input errors
        try:
            expense_amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, expense_amount))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    # Return list of expenses
    return expenses

# Define function to return the total expenses
def total_expense(expenses):
    return reduce(lambda total, expense: total + expense[1], expenses, 0)

# Define function to return the highest expense
def highest_expense(expenses):
    return reduce(lambda highest, expense: expense if expense[1] > highest[1] else highest, expenses)

# Define function to return the lowest expense
def lowest_expense(expenses):
    return reduce(lambda lowest, expense: expense if expense[1] < lowest[1] else lowest, expenses)

# Define main function to control the program
def main():

    # Prompt user for expenses
    expenses = get_expenses()

    # Stop program if no expenses were provided
    if not expenses:
        print("No expenses entered.")
        return

    # Get the total, highest, and lowest expenses
    total = total_expense(expenses)
    highest = highest_expense(expenses)
    lowest = lowest_expense(expenses)

    # Print output
    print(f"\nTotal Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

# Main
if __name__ == "__main__":
    main()