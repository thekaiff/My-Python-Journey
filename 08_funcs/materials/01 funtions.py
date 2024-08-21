"""
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a+b+c)/3

print(average)


a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a+b+c)/3

print(average)

"""


# # function defination:

def avg():
    """
    Description : This function will calculate average of given number.    
    Return : This function will return the average of given number.    
    """

    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a+b+c)/3

    print(average)
    return "hogyaaa!! "


# # function call: you can it multiple times!

a = avg()
print(a, "\nthank you!") 
# avg() 
# print("thank you!") 
# avg() 
# print("thank you!") 
# avg() 
# avg() 


# quick quiz

def gd():
    print("Good day!")

gd()



## why functions?(Interview Question)
# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible
