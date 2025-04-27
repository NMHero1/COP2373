# This program creates a database of Florida cities' population data for 2023,
# simulates 20 years of population growth at a 2% annual rate, and plots population growth using matplotlib.

# Import required libraries
import sqlite3
import matplotlib.pyplot as plt


# Define function to create the database and insert initial 2023 population data
def create_database():
    # Connect to (or create) a SQLite database
    conn = sqlite3.connect('population_NM.db')
    cursor = conn.cursor()

    # Create the 'population' table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')

    # Initial population data for 10 Florida cities in 2023
    florida_cities = {
        'Miami': 450000,
        'Orlando': 310000,
        'Tampa': 400000,
        'Jacksonville': 950000,
        'Tallahassee': 200000,
        'St. Petersburg': 260000,
        'Fort Lauderdale': 180000,
        'Sarasota': 60000,
        'Pensacola': 55000,
        'Gainesville': 140000
    }

    # Insert each city's data into the table
    for city, population in florida_cities.items():
        cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, 2023, population))

    # Commit changes and close connection
    conn.commit()
    conn.close()


# Define function to simulate 2% annual population growth for 20 years
def simulate_population_growth():
    # Connect to the database
    conn = sqlite3.connect('population_NM.db')
    cursor = conn.cursor()

    # Fetch the initial 2023 population data
    cursor.execute('SELECT city, population FROM population WHERE year = 2023')
    initial_data = cursor.fetchall()

    # Loop through each city and simulate growth for 2024-2043
    for city, population in initial_data:
        current_population = population
        for year in range(2024, 2024 + 20):
            # Calculate new population with 2% growth
            current_population = int(current_population * 1.02)
            # Insert the new year's data
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, current_population))

    # Commit changes and close connection
    conn.commit()
    conn.close()


# Define function to plot population growth for a selected city
def plot_population_growth():
    # List of available cities
    cities = [
        'Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee',
        'St. Petersburg', 'Fort Lauderdale', 'Sarasota', 'Pensacola', 'Gainesville'
    ]

    # Display city options to the user
    print("Choose a city from the following list:")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")

    # Prompt user to select a city by number
    try:
        choice = int(input("Enter the number corresponding to the city: "))
        if 1 <= choice <= len(cities):
            selected_city = cities[choice - 1]
        else:
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return

    # Connect to the database
    conn = sqlite3.connect('population_NM.db')
    cursor = conn.cursor()

    # Fetch population data for the selected city
    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
    data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Check if data is found and plot
    if data:
        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        # Plot population growth
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o')
        plt.title(f"Population Growth of {selected_city}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.grid(True)
        plt.show()
    else:
        print("No data found for the selected city.")


# Define the main function to control the program flow
def main():
    # Create the database and insert initial data
    create_database()

    # Simulate population growth for 20 years
    simulate_population_growth()

    # Plot population growth for the user's selected city
    plot_population_growth()


# Main
if __name__ == "__main__":
    main()
