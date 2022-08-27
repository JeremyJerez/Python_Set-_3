# Python_Intro
# Problem Set 
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "outdated" problem... a hard one in this stage of my learning
"""
Months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("date: ")
    try:
        month, day, year = date.split("/")
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
            break
    except:
        try:
            month_2, day_2, year = date.split(" ")
            for i in range(len(Months)):
                if month_2 == Months[i]:
                    month = i + 1
            day = day_2.replace(",", "")
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass

        
print(f"{year}-{int(month):02}-{int(day):02}")
