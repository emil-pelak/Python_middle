from datetime import datetime


def calculate_date_diff(date1, date2):
    # Convert the input strings to datetime objects
    date_format = "%Y-%m-%d"  # Format of the dates (change as per your input format)
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)

    # Calculate the date difference
    diff = datetime2 - datetime1

    # Return the difference in days
    return diff.days


# User input
print("Calculate difference between two dates.")
date1 = input("First date (YYYY-MM-DD): ")
date2 = input("Second date (YYYY-MM-DD): ")
diff_in_days = calculate_date_diff(date1, date2)
print(f"The difference between {date1} and {date2} is {diff_in_days} days.")
