# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    a = int(input("enter no. 1: "))
    b = int(input("enter no. 2: "))
    c = int(input("enter no. 3: "))
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
   

print(f"greatest is {greatest("","","")}")