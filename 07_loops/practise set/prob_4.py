# Write a program to find whether a given number is prime or not

# a = int(input("enter a given no.: "))

# if (a%2==0):
#     print("even no. ")

# else:
#     print("odd no. ")


a = int(input("enter a given no.: "))

for i in range (2, a):
    if( a % i == 0 ):
        print("this is not a prime no.") 
        break
else:
        print("this is a prime no. ")

