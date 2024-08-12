# We can primarily write a string in these three ways.
a ='kaif' # Single quoted string
b = "kaif" # Double quoted string
c = '''kaif''' # Triple quoted string

# strings are immutable

# string slicing: to get a part of a string, string can be sliced.

name = "Kaif Sayed"

nameshort = name[0:6]
print("name short: ", nameshort)
print("name length:", len(name))

character1 = name[3]
print(character1)

print("Negative indexing:")
print(name[-10:  ]) 
print(name[-8 :  ]) 
print(name[3  :-2]) 
print(name[-7 :-3]) 
print(name[   :-3]) 
 
print("slicing with skip value:")
a = "0,1,2,3,4,5,6,7,8,9"  # here even "," is considered as string
print(a[0:8:2])            #skiping the value by 2 no.s 
print("length:", len(a))            #skiping the value by 2 no.s 
print(a[0:8:2])            #skiping the value by 2 no.s 

b = "0123456789"

print("length:", len(b))
print(b[0:8:2])

d = "kaif sayed"
print(f"COUNT OF \' a\' IN KAIF SAYED IS : {d.count("a")}")