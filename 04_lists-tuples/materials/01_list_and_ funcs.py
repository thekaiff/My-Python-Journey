# # Python lists are containers to store a set of values of any data type.
# # list are mutable, it supports item assiggnment 


frnds = ["Apple", 302.3, 323 , False, 4, "kaif"] 
# print(frnds[0])

# frnds[0] = "banana"

# print(frnds[0])
print(frnds.index("Apple"))

# # # print(frnds[5])
# # print(frnds[0:4]) #slicing

# print(frnds)
# frnds.append("sayed") # adds item to the list
# print(frnds)  


# # other list functions:
li = [1, 23, 44, 5, 78, 103, 32, 11 ]

# li.sort()
# print(li)

# li.reverse()
# print(li)

print(li)
li.insert(2,55)   # 55 at index no. 2
li.insert (3,85)  # 85 at index no. 3
print(li)

print(li.pop(3))

li.remove(55)
print(li)
