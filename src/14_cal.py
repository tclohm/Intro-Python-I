"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

def isNumbers(num1, num2):
	try:
		return type(int(num1)) == int and type(int(num2)) == int and len(num1) == 2 and len(num2) == 4 and int(num1) <= 12 and int(num1) > 0
	except Exception as e:
		return False

def start():
	result = "Please provide a month and year in this format: MM YYYY or provide nothing. MM must be between 01-12."
	"""
	print the parameters
	"""
	cal = calendar.TextCalendar()
	if len(sys.argv) == 1:
		now = datetime.now()
		print(cal.formatmonth(now.year, now.month))
	elif len(sys.argv) == 3:
		(_, month, year) = sys.argv
		if isNumbers(month, year):
			user_chosen_month = int(month)
			user_chosen_year = abs(int(year))
			print(cal.formatmonth(user_chosen_year, user_chosen_month))
		else: 
			print(result)
	else:
		print(result)


start()