# def greet(name = "stranger"):
#     print(name)
# # function body
# greet() # name will be "stranger" in function body (default)
# greet("harry") # name will be "harry" in function body (passed)


def GoodDay(name, ending="thank you"):
    name = input("Enter your name: ")
    print(f"Good Day, {name} sir!")
    print(ending)

# GoodDay(name="", "thanks")   -throws error
GoodDay("", "thanks")
GoodDay("")
