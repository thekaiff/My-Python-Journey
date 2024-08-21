# . Write a python function which converts inches to cms

# cm = 10*inch

def i2c(inch):
    return  inch*2.54

n = int(input("enter a value of inch to convert in cm's: "))
print(f"{n} inch value in cm: {i2c(n)}")
