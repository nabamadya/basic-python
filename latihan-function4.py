import calendar

year = int(input(f"Enter year: "))
month = int(input(f"Enter month: "))
cal = calendar.month(year, month)
print(cal)

