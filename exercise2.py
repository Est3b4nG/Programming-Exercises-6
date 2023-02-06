"""
Created by (Esteban Gómez) in  ${2022}
"""
"""Create a program with the following functions:
a. createListNumbers: Creates a list of 10 random elements all even numbers and returns
it.
b. calculateFigures: receives a list as parameter and calculates the maximum, minimum
and average values of the list. It returns the calculated values.
"""

def createListNumber():
    """"@This function create a list of 10 random elements all even"""
    import random
    list_of_numbers=[]
    while len(list_of_numbers)<10:
        number= random.randint(1,100)
        if number%2==0:
            list_of_numbers.append(number)
    return list_of_numbers


def calculateFigures(list1=list):
    """"@This function recieves a list as a parameter and calculate de maximum, minimum and avergae
    "@param1=list"""
    Max=list1[0]
    Min= list1[0]
    Sum=0

    for i in list1:
        if i>Max:
            Max=i
        elif i<Min:
            Min=i
        Sum+= i
    Average=Sum/len(list1)
    return Max, Min, Average



final_list= createListNumber()
print(final_list)

res= calculateFigures(final_list)
print("The Max is:", res[0])
print("The Min is:", res[1])
print("The avergae is:", res[2])






