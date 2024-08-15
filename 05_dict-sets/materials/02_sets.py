# # Set is a collection of well defined objects which are non-repetitive,unindexed, unodered unique elements.
# # sets are immutable and subscriptable, meaning we can retrive elements thro indexing and cant assign items bcoz of it.

# set1 = {1, 23, 4, 5, 6.6, "df", 5, 5, 5, False}

# empty = set() # dont use set1= {}, as it will create an empty dict.
# print(type(empty))

# print(set1) 


# # OPERATIONS:


# # Adding Elements:
# set1.add(76)
# # print(set1.add(76)) # returns none 


# # Removing Elements:
# set1.remove(1)
# print(set1)

# set1.pop() # Removes and returns an arbitrary element from the set.
#            # Raises KeyError if the set is empty.
# print(set1) 

# set1.discard(5) #Removes a specified element from the set if it is present, but
# set1.discard(7) # does not raise an error if the element is not found.
# print(set1)


# # Combining Sets:

set1 = {1, 23, 4, 5, 6.6, "df", 5, 5, 5, False}
set2 = {1, 3, 4, 67, 5, True, "htg", 6, False}
print(set1.union(set2))
# Returns a new set containing all distinct elements from both sets.

# print(set1.intersection(set2))
# print(set1) 
# # adding elements from another set (or any iterable) which are same.
# print(set1.intersection_update(set2))
# print(set1)
# # Updates the set, adding elements from another set (or any iterable) which are same.

print(set1.difference(set2))
# gives the elements which are same from both the sets

# # print(set1.issuperset("df")) 
# print(len(set1)) 
