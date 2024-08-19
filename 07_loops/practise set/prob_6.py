# Write a program to calculate the factorial of a given number using for loop.


n  = int(input("Enter a no: "))

fac = 1

for i in range (1, n+1):
    fac = fac * i

print(f"your factorial of {n} is {fac}")