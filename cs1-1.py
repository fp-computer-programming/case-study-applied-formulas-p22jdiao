# JD 10/12/2021

x1 = int(input("Please enter the x coordinate of the first point: "))

y1 = int(input("Please enter the y coordinate of the first point: "))

x2 = int(input("Please enter the x coordinate of the second point: "))

y2 = int(input("Please enter the x coordinate of the second point: "))

x_diff = x2 - x1

y_diff = y2 - y1

distance_sq = x_diff ** 2 + y_diff ** 2

distance = distance_sq ** (1/2)

print(distance)