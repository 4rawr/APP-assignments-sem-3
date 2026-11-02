import numpy as np

sensor_readings = np.array([10, 12, 23, 34, 56, 67, 69, 78, 89, 90])

first_4 = sensor_readings[4:]
mid_6_to_9 = sensor_readings[6:10]

sum = np.sum(sensor_readings)
avg = np.mean(sensor_readings)
max = np.max(sensor_readings)
min = np.min(sensor_readings)

broadcasted_readings = sensor_readings + 3

print("Readings:", sensor_readings)
print("First 4 readings:", first_4)
print("Readings from 6 to 9:" mid_6_to_9)
print("Sum:", sum)
print("Average:", avg)
print("Maximum:", max)
print("Minimum:", min)
print("Broadcasted Readings:", broadcasted_readings)



"""
OUTPUT :- 

PS C:\Users\N51310\Downloads> python ADT25SOCB0206_4_10.py
Readings: [10 12 23 34 56 67 69 78 89 90]
First 4 readings: [10 12 23 34]
Readings from 6 to 9: [67 69 78 89]
Sum: 528
Average: 52.8
Maximum: 90
Minimum: 10
Broadcasted Readings: [13 15 26 37 59 70 72 81 92 93]
"""
