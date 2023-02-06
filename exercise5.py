"""
Created by (Esteban Gómez) in  ${2022}
"""

"""Generate a function that allows you to correctly write uppercase letters in a given text: The first
character of the string must be written in uppercase; also the “i” letter when it is followed by a
blank space and the previous one is a blank space too. In addition, the first non-blank character
after a ".", "!" or "?" For example, if the function is provided with the string "what time do i
have to be there? what is the address?", Then it should return the string "What
time do I have to be there? What is the address?" Include a program that
reads a user string, capitalizes the appropriate letters using this function and displays the result
on the screen"""

def uppercase_function(text1=str):
    """This function teach how to properly use capital letters"""
    i_mayus=text1.replace(" i ", " I ")
    list1=list(i_mayus)
    list1[0]=list1[0].upper()
    for elem in list1:
        if elem=="." or elem=="!" or elem== "?":
            where=list1.index(elem)
            list1[where+2]= list1[where+2].upper()
    Initialize1= ""
    final_sentence=Initialize1.join(list1)
    return final_sentence

text=str(input("Introduce your text: "))

print(uppercase_function(text))