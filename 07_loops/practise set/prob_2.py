# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
l = ["kaif", "tom", "shana", "shurti", "zakir"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello, {name}")
