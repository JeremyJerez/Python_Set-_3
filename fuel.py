# Python_Intro
# Problem Set 3
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Fuel Gauge" problem
"""
while True:
    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")
        num = int(numerator)
        den = int(denominator)
        F = num / den
        if F <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
# change to integer percentage
p = int(F * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
