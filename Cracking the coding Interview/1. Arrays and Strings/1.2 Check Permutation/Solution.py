def permuation_check(str1,str2):

    lowered_str1 = "".join(str1.lower().split())
    lowered_str2 = "".join(str2.lower().split())

    if len(lowered_str1) != len(lowered_str2):
        return False
    char_map = {}
    for i in lowered_str1:
        if i not in char_map:
            char_map[i] = 1
        else :
            char_map[i] += 1
        
    for i in lowered_str2:
        if i not in char_map:
            return False
        else:
            char_map[i] -= 1

    is_permuation = all(count==0 for count in char_map.values())
    if is_permuation:
        return True
    else:
        return False

str1 = input("Enter first String : ")
str2 = input("Enter second String : ")
if permuation_check(str1,str2):
    print("String are permuation of each other ")
else :
    print("Strings are diffrent")