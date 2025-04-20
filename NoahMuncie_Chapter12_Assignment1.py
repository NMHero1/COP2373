# This program is designed to load student exam grades from a CSV file, calculate statistics, and determine pass/fail counts for each exam and overall performance using NumPy.

# Import numpy for numerical computations
import numpy as np


# Define function to load exam data from a CSV file
def load_exam_data(filename):
    # Load only the exam columns (skipping names) from the CSV, skipping header row
    data = np.genfromtxt(filename, delimiter=",", skip_header=1, usecols=(2, 3, 4))
    return data


# Define function to print statistics for each exam and overall
def print_stats(data):
    # Get number of exams (columns)
    num_exams = data.shape[1]

    # Loop through each exam and calculate statistics
    for i in range(num_exams):
        exam = data[:, i]
        print(f"\nStatistics for Exam {i + 1}:")
        print(f"  Mean: {np.mean(exam):.2f}")
        print(f"  Median: {np.median(exam):.2f}")
        print(f"  Std Dev: {np.std(exam):.2f}")
        print(f"  Min: {np.min(exam)}")
        print(f"  Max: {np.max(exam)}")

    # Flatten the 2D array into 1D to calculate overall statistics
    all_grades = data.flatten()
    print("\nOverall Statistics Across All Exams:")
    print(f"  Mean: {np.mean(all_grades):.2f}")
    print(f"  Median: {np.median(all_grades):.2f}")
    print(f"  Std Dev: {np.std(all_grades):.2f}")
    print(f"  Min: {np.min(all_grades)}")
    print(f"  Max: {np.max(all_grades)}")


# Define function to calculate and display pass/fail statistics
def pass_fail_stats(data, passing_score=60):
    # Get number of exams
    num_exams = data.shape[1]

    # Initialize total pass counter
    total_pass = 0

    # Calculate total number of grades
    total_grades = data.size

    # Print header
    print("\nPass/Fail Counts Per Exam (Passing: 60+):")

    # Loop through each exam to count passes and fails
    for i in range(num_exams):
        passed = np.sum(data[:, i] >= passing_score)
        failed = data.shape[0] - passed
        total_pass += passed
        print(f"  Exam {i + 1}: Passed = {passed}, Failed = {failed}")

    # Calculate and print overall pass percentage
    pass_percentage = (total_pass / total_grades) * 100
    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")


# Define main function to control the program
def main():
    # Set the filename (ensure your CSV is named this or change it here)
    filename = "grades.csv"

    # Load the exam data from the file
    data = load_exam_data(filename)

    # Print the first few rows to understand the structure
    print("First few rows of exam data:")
    print(data[:5])  # Display first 5 rows

    # Print statistics for each exam and overall
    print_stats(data)

    # Print pass/fail stats
    pass_fail_stats(data)


# Main
if __name__ == "__main__":
    main()
