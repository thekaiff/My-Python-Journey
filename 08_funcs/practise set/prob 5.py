'''

Write a python function to print first n lines of the following pattern:
***
**    - for n = 3
*

'''

def pattern(n):
    if(n==0):
        return # to exit
    print("*"*n)
    pattern(n-1)


n = int(input("enter value of n for pattern: "))
pattern(n)
# print(f"your pattern:\n{pattern(n)}")
