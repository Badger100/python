import calendar
m = int(input("Enter month: "))
y = int(input("Enter year: "))

print(calendar.prmonth(y, m))
text_calendar = calendar.TextCalendar(y)
text_calendar.pryear(y)
print(text_calendar)
