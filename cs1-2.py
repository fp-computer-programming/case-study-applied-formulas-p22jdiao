# Author: JD 10/12/2021

p = float(input("The principle investment: "))

r_per = float(input("The annual interest rate in percentage: "))

r = r_per / 100

t = int(input("The number of years for the investment: "))

n = 12

a = p * (1 + r / n) ** (n * t)

print(a)