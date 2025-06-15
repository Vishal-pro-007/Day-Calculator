import datetime

while True:  # loop begins here
    date = input("Enter date (YYYY-MM-DD) or type 'exit' to quit: ")
    
    if date.lower() == 'exit':  # must come before the try
        break

    try:
        year, month, day = map(int, date.split("-"))
        day_name = datetime.date(year, month, day).strftime("%A")
        print("Day of the week:", day_name)
    except:
        print("Invalid input. Try again.")

