import datetime

while True:
    try:
        date_str = input("Enter the date in YYYY-MM-DD format\n")
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        break
    except ValueError:
        print("Invalid date format! Please enter the date in the format YYYY-MM-DD.")

day_of_week = date_obj.strftime('%A')
print(f"The day of the week for {date_str} is {day_of_week}")