# 1. Write a program to find the greatest of four numbers entered by the user.

a = int(input("enter a no.: "))
b = int(input("enter a no.: "))
c = int(input("enter a no.: "))
d = int(input("enter a no.: "))

if(a>b and a>c and a>d ):
    print(a, " is greater")

elif(b>a and b>c and b>d):
    print(b, "is greater")

elif(c>a and c>b and c>d):
    print(c, "is greater")

elif(d>a and d>b and d>c):
    print(d, "is greater")
