# # Write a python program to display a user entered name 
# # followed by Good Afternoon using input () function.

# name = input("ENTER YOUR NAME:")
# # print("Good Afternoon", name.title())
# print(f"Good Afternoon {name.title()}") #fstring



# # Write a program to fill in a letter template given below 
# # with name and date.

# letter = '''Dear <|Name|>,\nYou are selected!\n<|Date|>'''
# print(letter.replace("<|Name|>", "Kaif").replace("<|Date|>", "26 June 2024"))
# #this is chaining of func



# # Write a program to detect (find) double space in a string.

# name ="Kaif is a good boy and  bad man"
# # print(name.rfind("d "))
# print(name.find("  "))



# # Replace the double space from problem 3 with single spaces.

# print(name.replace("  ", " "))
# print(name) # string are  immutable, this doesnt change og  by
#             # runnning a func on them



# Write a program to format the following letter using escape 
# sequence characters.

letter = "Dear Kaif, \n \t this python course is nice. \nThanks!"
print(letter.title())
