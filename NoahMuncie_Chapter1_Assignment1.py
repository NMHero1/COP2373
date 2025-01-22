# The program is designed to sell a limited number of 20 cinema tickets to buyers. Each buyer is allowed to purchase up to 4 tickets and the remaining ticket count is printed after every sale.

# Define global variables
tickets = 20
LIMIT = 4

# Function to get and validate user input
def get_input():

	# Prompt the user for input
	userInput = input("How many tickets would you like to purchase?\n")

	# Check if the user input is a valid integer
	try:
		quantityDesired = int(userInput)
		return quantityDesired

	except ValueError:
		print("\nInvalid input. Please enter a valid integer.")
		return get_input()

# Function to process purchases and perform arithmetic
def process_purchase(quantityDesired: int):
	global tickets

	# Check if the desired quantity is within the limits
	if quantityDesired > 0 and quantityDesired <= 4:

		# Check if quantity is less than total
		if quantityDesired <= tickets:
	
			# Perform arithmetic
			tickets -= quantityDesired
	
			# Print remaining tickets
			print(f"\nSuccessfully purchased {quantityDesired} ticket(s)!")
			print(f"{tickets} tickets remain.")

			pass
	
		else:
			print(f"\nOnly {tickets} tickets remain, please enter a smaller number.")

	else:
		print(f"\nPlease enter a number between 1 and {LIMIT}.")

	pass

	
# Main function
def main():
	global tickets

	while tickets > 0:
		purchaseAmount = get_input()
		process_purchase(purchaseAmount)

	print(f"\nAll tickets have sold out!")

main()