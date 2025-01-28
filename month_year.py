import calendar

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

calendar.setfirstweekday(calendar.SUNDAY)

mycal = calendar.month(year,month)


print(mycal)
