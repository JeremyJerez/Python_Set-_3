# Python_Intro
# Problem Set 3
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Grocery List" problem
"""
grocery = {} #A brand new dict
while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key)
        break
