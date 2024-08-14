# A Tuple is a datatype in python which is a collection of diff. data types separated by "," as well as it is immutable, indexed but does not support item assignment

a = (1, 2, 3, "ddvf", 56.6,True )
print(type(a))

b = (1) # not a tuple with single element.
print(type(b)) # gives type int.

c = (1,) # single value tuple
print(type(c)) # gives type tuple

a[0] = (4,) #doesn't support item assignment


