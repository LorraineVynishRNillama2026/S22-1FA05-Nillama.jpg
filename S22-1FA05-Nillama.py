import math


x1 = float(input("Please input first x coordinate: "))
y1 = float(input("Please input first y coordinate: "))
x2 = float(input("Please input second x coordinate: "))
y2 = float(input("Please input second y coordinate: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print("Distance: ", distance)
