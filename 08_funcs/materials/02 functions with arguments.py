def gd(name, end ):
    # print("Good day!", name)
    print(f"Good day! {name} ")
    # print("Good day! " + name)
    print(end)

gd("kaif", "thankyou") # position argument
gd("sayed", "shukriya")


def gd(name, end="hahaha!!" ): # key argument
    print(f"Good day! {name} ")
    print(end)

gd("kaif", "thankyou")
gd("sayed", "shukriya")
gd("wanna", )



# distinguishing between positional and key arguments : 
def hello(*args, **kwargs) :     # *agrs : positional, **kwargs : key
    print(f"\npositional : {args}")
    print(f"\nkey : {kwargs}\n")

# hello("kaif", "sayed", "anis", age=22, yob=2002)

# another way to do it : 
lst = list(("kaif", "anis", "sayed")) # converting list in tuple
dict_val = {'age': 22, "yob": 2002}
# hello(*lst,**dict_val)

hello("kaif","anis","!","2", 55, age=22,dob=2002)





