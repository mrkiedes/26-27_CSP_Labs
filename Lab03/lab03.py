milliseconds = 10000123

seconds = milliseconds // 1000
milli_seconds_left = milliseconds % 1000

hours = seconds // 3600
seconds_left = seconds % 3600

minutes = seconds_left // 60
seconds_left = seconds_left % 60

print("Starting milli-seconds: \t\t" + str(milliseconds))
print("Hours: \t\t\t\t\t\t\t" + str(hours))
print("Minutes: \t\t\t\t\t\t" + str(minutes))
print("Seconds: \t\t\t\t\t\t" + str(seconds_left))
print("Milli Seconds: \t\t\t\t\t" + str(milli_seconds_left))