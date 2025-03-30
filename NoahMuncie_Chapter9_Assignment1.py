# This program is designed to manage bank accounts by allowing users to deposit, withdraw, adjust interest rates, and calculate interest over time.

# Define the BankAcct class
class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        # Initialize account details
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Define method to adjust the interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Define method to deposit funds into the account
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive.")

    # Define method to withdraw funds from the account
    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Define method to check account balance
    def get_balance(self):
        return self.amount

    # Define method to calculate interest earned over a given number of days
    def calculate_interest(self, days):
        return self.amount * (self.interest_rate / 100) * (days / 365)

    # Define method to display account details
    def get_account_details(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%")

# Define function to test BankAcct class
def test_bank_account():
    # Create a test account
    acct = BankAcct("John Doe", "123456789", 1000.00, 3.5)

    # Display initial account details
    print(acct.get_account_details())

    # Test deposit method
    acct.deposit(500)
    print("After deposit:")
    print(acct.get_account_details())

    # Test withdrawal method
    acct.withdraw(300)
    print("After withdrawal:")
    print(acct.get_account_details())

    # Test interest calculation method
    interest = acct.calculate_interest(30)
    print(f"Interest earned in 30 days: ${interest:.2f}")

    # Test interest rate adjustment method
    acct.adjust_interest_rate(4.0)
    print("After adjusting interest rate:")
    print(acct.get_account_details())

# Run the test function to validate the BankAcct class
test_bank_account()