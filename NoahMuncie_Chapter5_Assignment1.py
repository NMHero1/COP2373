# This program is designed to take user input in the form of phone numbers, social security numbers, and zip codes and validate it

# Import regular expressions
import re

# Define function to validate phone numbers
def validate_phone_number(phone):

    # Define pattern
    pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

# Define function to validate social security numbers
def validate_ssn(ssn):

    # Define pattern
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))

# Define function to validate zip codes
def validate_zip_code(zip_code):

    # Define pattern
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))

# Define main function to control the program
def main():

    # Get user input
    phone = input("Enter a phone number (format: (123) 456-7890): ")
    ssn = input("Enter a Social Security Number (format: 123-45-6789): ")
    zip_code = input("Enter a ZIP code (format: 12345 or 12345-6789): ")

    # Print results
    print("\nValidation Results:")
    print(f"Phone Number Valid: {validate_phone_number(phone)}")
    print(f"SSN Valid: {validate_ssn(ssn)}")
    print(f"ZIP Code Valid: {validate_zip_code(zip_code)}")

# Main
if __name__ == "__main__":
    main()