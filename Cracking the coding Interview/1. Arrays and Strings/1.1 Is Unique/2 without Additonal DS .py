def is_unique_withoutDS(val):
    sorted_val = "".join(sorted(val.lower()))
    for i in range(len(sorted_val) - 1):
        if sorted_val[i] == sorted_val[i + 1]:
            return False
    return True

val = input("Enter the string: ")
if is_unique_withoutDS(val):
    print("All characters are unique")
else:
    print("Characters are not unique")