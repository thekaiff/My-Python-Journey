# # Write a program to create a dictionary of Hindi words with values as their English
# # translation. Provide user with an option to look it up!

# words = {
#     "chand" : "Moon",
#     "suraj" : "Sun" ,
#     "billi" : "cat" ,
#     "kutta" : "dog" ,
# }

# word = input("Enter a word to translate in English: ")
# print(words[word])



# # Write a program to input eight numbers from the user and display all the unique
# # numbers (once).

# s = set()

# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))
# no = input("Enter a no.: ")
# s.add(int(no))

# print(s)



# # Can we have a set with 18 (int) and '18' (str) as a value in it?

# s1 = set()
# s1.add("18")
# s1.add(int(18))

# print(s1)
# # yes we  can



# # What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?
# print(len(s)) #returns 2

# bcoz comparison operator checks if the value are numarically same or not, even if it is a data type doesnt matter
# bcoz of the dynamic typing and flexible approach to numeric types of language



s2 = {}
# What is the type of 's'?
print(type(s2))



# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = { }

name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})
name = input("Enter your name: ")
lang = input("Enter your fav language: ")
d.update({name:lang})


print(d) 



# If the names of 2 friends are same; what will happen to the program in problem
# 6?

# it will update the frnds value by last value entered coz of update method



# If languages of two friends are same; what will happen to the program in problem
# 6?

# this wont effect the program, both will have same value. coz it has identifier key



# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# s[4][0]=9
# print(s)

# cant update, bcoz we cant conclude list in a set and we cant perform indexing

# no, you cant change the value inside a list contained in a set in python. 
# in fact, you cannot even have a list as an element in a set bcoz sets in python requires all the
# elements to be immutable and hashable, list are mutable but non hashable, so the cannot be added to a set.