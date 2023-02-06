"""
Created by (Esteban Gómez) in  ${2022}
"""

"""Create a function that generates a random number between a minimum and a maximum. It will
have a third parameter to state if it must return an integer, float or complex number"""

import random

def function_random(minimum=float, maximum=float, type=float):
    """@ This will state if it is a float, integer or complex number"""

    if type == int or type== float or type==complex:
        if minimum // 1 == minimum and maximum // 1 == maximum:
            number3 = random.randint(minimum, maximum)
        else:
         number3= random.uniform(minimum,maximum)
        return number3
    else:
        raise TypeError("The maximum and minimum can't be a string or bool")

try:
    minimum1=float(input("Introduce a minimum: "))
    maximum1= float(input("Introduce the maximum: "))
    type1=type(maximum1)

    final_number= function_random(minimum1,maximum1,type1)
    print(final_number)
except:
    raise TypeError("The maximum and minimum can't be a string or bool")