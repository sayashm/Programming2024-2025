# https://dodona.be/nl/courses/4157/series/46289/activities/1765918609

temperatures = []
t = 'start'

# Read the temperature input
while t:
    t = input('Temperature? ')
    if t == 'stop':
        break
    else:
        temperatures.append(float(t))

# Variables to track tropical days (>= 30°C) and summer days (>= 25°C)
consecutive_days = 0
tropical_days = 0
heat_wave_found = False

# Loop through the list of temperatures
for i in range(len(temperatures)):
    if temperatures[i] >= 25:
        consecutive_days += 1

        # Check if this is a tropical day
        if temperatures[i] >= 30:
            tropical_days += 1
    else:
        # If we have a valid period with >= 5 consecutive days and >= 3 tropical days
        if consecutive_days >= 5 and tropical_days >= 3:
            heat_wave_found = True
            break
        # Reset counters if less than 25°C encountered
        consecutive_days = 0
        tropical_days = 0

# Check the final period at the end of the list
if consecutive_days >= 5 and tropical_days >= 3:
    heat_wave_found = True

# Output result
if heat_wave_found:
    print("heat wave")
else:
    print("no heat wave")






