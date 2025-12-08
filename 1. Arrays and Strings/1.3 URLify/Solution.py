def space_replacer(val):
    return val.replace(" ","%20")

val = input("Enter the string: ")
print("New string is : ",space_replacer(val))