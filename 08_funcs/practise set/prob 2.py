# Write a python program using function to convert Celsius to Fahrenheit.

# c = 5*(f-32)/9
    # f = int(input("enter fahrenheit value: "))
    # c = 5*(f-32)/9

def f2c(f):
    return 5*(f-32)/9

f = int(input("enter fahrenheit value: "))
c = f2c(f)
print(f"{round(c,2)}°C")
