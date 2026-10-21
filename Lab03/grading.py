Starting_Milliseconds = 10000123
seconds = Starting_Milliseconds // 1000
Hours = seconds // 3600
seconds_left = seconds % 3600
Minutes = seconds_left // 60
Seconds = seconds_left % 60
milli_seconds_left = Starting_Milliseconds % 1000


print("Starting milliseconds: ", Starting_Milliseconds)
print("Hours: ", Hours)
print("Minutes: ", Minutes)
print("Seconds: ", Seconds)
print("Milliseconds left: ", milli_seconds_left)