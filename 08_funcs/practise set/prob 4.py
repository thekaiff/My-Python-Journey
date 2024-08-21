""""
Write a recursive function to calculate the sum of first n natural numbers.

sum(n) = sum(n-1)+n

"""

def sum(n):
    if (n==1):
        return 1
    elif(n<1):
        return n
    return sum (n-1) + n
n = int(input("enter a no.: "))
print(f"sum of number is: {sum(n)}")
