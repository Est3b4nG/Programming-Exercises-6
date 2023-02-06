"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Write a function that determines how many days there are in a particular month. The function
will receive two parameters: the month, as an integer between 1 and 12, and the year as a
four-digit integer. Consider the existence of leap years. Create a main program that reads a
month and a year from the keyboard and displays the number of days in that month on the
screen.
"""

def time_function(month=int, year=int):
    """@This function will recieve a month and a year, and will tell you how many days it have"""
    if month<=12:
        if month==1:
            day=31
        if month==2:
            if year % 4 == 0 or year % 400 == 0:
                day=29
            else:
                day=28
        if month==3:
            day==31
        if month==4:
            day==30
        if month==5:
            day=31
        if month==6:
            day=30
        if month == 7:
            day = 31
        if month == 8:
            day = 31
        if month==9:
            day=30
        if month==10:
            day=31
        if month==11:
            day=30
        if month==12:
            day=31
        return day
    else:
        raise TypeError("There are not more than 12 months")


user_month=int(input("Which month: "))
user_year=int(input("Which year: "))

print(time_function(user_month, user_year))