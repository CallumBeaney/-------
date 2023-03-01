# This program uses the datetime module in Python to get the current date and time. 
# It then uses the weekday() method to get the day of the week as an integer, where Monday is 0 and Sunday is 6. 
# Finally, it converts the integer to a string representation of the day of the week using a list of day names, and prints the result.

import datetime # import a pre-loaded library for handling date/time information

# Get the current date and time
now = datetime.datetime.now()

# Get the day of the week as an integer (Monday is 0, Sunday is 6)
day_of_week = now.weekday()

# Convert the integer to a string representation of the day of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_name = days[day_of_week]

# Print the day of the week
print("Today is", day_name)
