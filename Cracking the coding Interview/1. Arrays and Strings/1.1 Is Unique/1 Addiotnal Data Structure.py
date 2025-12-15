# Implement an algorithm to determine if a string has all unique characters. What if you 
# cannot use additional data structures? 


def is_unique(val):
    lower_val = val.lower()
    if len(lower_val) == len(set(lower_val)):
        return True
    else:
        return False 

val = input("Enter the string: ")
if is_unique(val):
    print("All characters are unique")
else:
    print("Characters are not unique")
