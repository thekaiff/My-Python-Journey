t1 = (1, 2, False, 44.4, 2, 2, 2, 3, "haha")
print(t1, type(t1))

# we can use tuple to find-out how many times an element is occuring in it by:
no = t1.count(2)
print(f"count of value 2 in t1:,{no}")



indx = t1.index(44.4)
print("index value of 44.4: ",indx) 



# Operation on tuples:

# tuple concatination:
t2 = ("Ddd", 23, 3, 3, 43.44, True) 
print ("concatination: \n", t1 + t2 ) 
print(t1.__add__(t2))

# tuple repitition:
print("\nt2 rep by 2: ",t2*2)

# membership: check whether if the value exists in a tuple
print("membrshp of 4: ", 4 in t1) 
print("membrshp of 3: ", 3 in t1) 

# length:
print("len of t1: ", len(t1))

# # min max:
# print("min", min(t1))
# print("max", max(t1))
# # wont give op coz of it contains value btwn instance of string and bool

#slicing:
print("slicing value: ", t1[1:5])

#unpacking:
t3 = (1,2,3)
a, b, c = t3
print("unpacking values: " , a,b,c)

# min max:
print("min: ", min(t3))
print("max: ", max(t3))
