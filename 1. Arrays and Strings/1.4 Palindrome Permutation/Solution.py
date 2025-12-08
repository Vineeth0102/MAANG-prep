def palindrom_check(val):
    lowered_val = "".join(val.lower().split())
    char_count = {}
    for i in lowered_val:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    count = 0
    for val in char_count.values():
        if val%2!=0 and count != 2:
            count += 1
        elif count == 2:
            return False
    return True


val = input("Enter the string : ")
if palindrom_check(val):
    print("Given String can be a palindrom")
else:
    print("Given string cannot be a plindrom")
