# dictionary is a collection of datatype which stores value in key value pairs,
# it is unodered, mutable, indexed and cannot contain duplicate keys

empty = { } # Empty dictionarie

marks = {
    "kaif" : 99.99,
    "sayed": 100  ,
    "motaz": 85   ,
    "tom"  : 24   ,
    "list" : [1,2,3],
      35   : "suresh"
}

# print(marks, type(marks))
print(marks[ "list" ]) # for indexing, we use keyword not numbers.

k = dict(kaif=99.99,motaz=85, suresh = "35")
print(k)
# METHOD:

print(marks.items()) # gives key-values pair in tuple format.
print(marks.values()) 
print(marks.keys())

marks.update({"kaif": 97, "lana":101})

# print(marks.get("kaif2")) # prints none
# print(marks["kaif2"])     # returns an error

print(marks.pop("tom", "def1")) # remove specified key and return the corresponding value.
print(marks.popitem())          # removes and returns a (key:value) pair, pairs are returned in LIFO format.

print(len(marks)) 
print(marks) 

# iteration:

for x in marks.keys(): # same as for x in marks.keys:
    print(x)

for x in marks.values():
    print(x)

for x in marks.items():
    print(x)

# Adding elements in dict:
marks["chapad chapad"]= 100
marks[12]="lala"
print(marks)

# nested dict:
model1 = {"mercedes" : 1960 }
model2 = {"mustang"  : 1969 }
model3 = {"bmw xm"   : "m340i" }

car_types = {"car1":model1, "car2":model2, "car3":model3}
print(car_types)

# nested dict indexing:
print(car_types["car1"])
print(car_types["car1"]["mercedes"])
