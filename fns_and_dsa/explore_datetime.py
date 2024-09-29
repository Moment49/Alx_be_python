from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

display_current_datetime()



def calculate_future_date(future_days):
    # Get the current date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=future_days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days)
