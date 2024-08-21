# Write a python function to remove a given word from a list ad strip it at the same
# time.

def remv(l, word):
    n = []
    for item in l:
        # print(f"list before: {l}")
        if not(item == word):
            n.append(item.strip(word))
        # l.remove(word)
    return n
        
l = ["kaif","sayed","if","cliff"]
n = input("enter a word: ")

print(f"list before : {l}")
print(f"list after : {remv(l,n)}")


    