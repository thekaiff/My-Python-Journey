# # mostly used funcs. to perform operations and to manipulate strings:

name = "kaif anis sayed      "

# length function():
print(len(name))

# endswith():
print("endswith:")
print(name.endswith("ed"))
print(name.endswith("ed."))

# # startswith():
# print("startswith:")
# print(name.startswith("anis"))
# print(name.startswith("kai"))

# print(name)

# # str.upper()
# print(name.upper())

# # str.lower()
# print(name.lower())

# # capitalized
# print(name.capitalize())

# # str.title
# print(name.title())

# str.strip()
print(name.strip())

# str.split(separator): Splits the string into a list of substrings 
# separated by the specified separator (default is whitespace).
print(name.split("."))

# str.join(iterable): Concatenates elements of an iterable (such as a list) into a 
# single string, with the original string as a separator.
lst = ["this", "is", "my", "code" ]
print(".".join(lst))
print("".join(name))

# str.find(sub) and str.rfind(sub):
# Returns the lowest (leftmost) and highest (rightmost) indices
# where substring sub is found in the string, or -1 if not found.
print(name.find("a"))
print(name.rfind("a"))

# str.replace(old, new): Returns a copy of the string with all 
# occurrences of substring old replaced by new.
print(name.replace("sayed", "abdul khuddus sayed"))

print("noice, very noice job!")