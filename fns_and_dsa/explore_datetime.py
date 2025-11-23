from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Part 1: Display current date and time
display_current_datetime()

# Part 2: Calculate a future date
days_input = input("Enter the number of days to add to the current date: ")
try:
    days_number = int(days_input)
    calculate_future_date(days_number)
except ValueError:
    print("Invalid input. Please enter an integer number of days.")