# Write a program to print multiplication table of n using for loops in reversed
# order.


a = int(input("enter a no.: "))

for i in range (1, 11):
    print(f"{a} x {11-i} = {a*(11-i)}")