# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as function

# 5! = 5x4x3!
# factorial(n):
# factorial(0):1
# factorial(1):1
# factorial(5) = 5x4x3!
# factorial(n) = n * factorail (n-1)


def factorial(num):
    if(num==0 or num==1):
        return 1
    return num*factorial(num-1)

num = int(input("Enter a number: "))
print(f"The factorial of the number {num} is {factorial(num)}")