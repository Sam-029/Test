'''
Subtracting the dates and getting difference (string into dd/mm/yy format)
'''
from datetime import datetime
def calculate_days_lived(input_date_str, current_date_str):
    # Convert string input to datetime objects
    input_date = datetime.strptime(input_date_str, "%d-%m-%Y")  
    current_date = datetime.strptime(current_date_str, "%d-%m-%Y")

    difference = current_date - input_date
    return difference.days

receive_date = input("Enter your birthdate (dd-mm-yyyy): ")
today_input = input("Enter today's date (dd-mm-yyyy): ")

days_lived = calculate_days_lived(receive_date, today_input)
print(f"lived {days_lived} days.")
