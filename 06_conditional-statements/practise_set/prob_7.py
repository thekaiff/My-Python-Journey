# Write a program to find out whether a given post is talking about "kaif" or not.

a = input("Enter a post: ")

if ("kaif" in a.lower() ):
    print("This post is about kaif.")

else:
    print("This post is not about kaif.")