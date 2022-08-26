# Problem Set 3
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Felipe’s Taqueria" problem
"""
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total_amount = 0

while True:
    try:
        Item = input("Item ").title()
        if Item in menu:
            total_amount += menu[Item]
            print("Total: $", "{:.2f}".format(total_amount))#"{:.2f}" to use two decimal points
    except EOFError:
        print()
        break#ctrl + z then Enter
