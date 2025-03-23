# This program is designed to allow teachers the option to either write or read students' grades to/from a CSV file

# Import CSV
import csv

# Define function to write grades to grades.csv
def write_grades():

    # Define file name
    filename = "grades.csv"

    # Get the number of students
    num_students = int(input("Enter the number of students: "))

    # Open the file in write mode
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Get student information
        for _ in range(num_students):
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write student record to CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # Print output
    print(f"\nData successfully written to {filename}.")

# Define function to read grades from grades.csv
def read_grades():

    # Define file name
    filename = "grades.csv"

    # Try block to catch exceptions
    try:

        # Open the file in read mode
        with open(filename, mode="r") as file:
            reader = csv.reader(file)

            # Read and print contents in tabular format
            data = list(reader)

            if len(data) == 0:
                print("The file is empty. Please add data first.")
                return

            # Print formatted table
            print("\n{:<15} {:<15} {:<10} {:<10} {:<10}".format(*data[0]))  # Header
            print("-" * 60)
            for row in data[1:]:
                print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))

    except FileNotFoundError:
        print("\nError: grades.csv file not found. Please enter student data first.")

# Define main function
def main():

    # Repeat while true
    while True:
        print("\nChoose an option:")
        print("1 - Enter student grades (write to file)")
        print("2 - Display student grades (read from file)")
        print("3 - Exit")

        # Get user input
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            write_grades()
        elif choice == "2":
            read_grades()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Main
main()