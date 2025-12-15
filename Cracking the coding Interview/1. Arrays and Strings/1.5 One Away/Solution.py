def one_way(str1,str2):
    lowered_str1 = "".join(str1.lower().split())
    lowered_str2 = "".join(str2.lower().split())

    char_count = {}
    for i in lowered_str1:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i in lowered_str2:
        if i in char_count:
            char_count[i] -= 1
        else:
            char_count[i] = 1
    
    count = 0
    for i in char_count.values():
        count += i
    
    if count > 1 or count < -1:
        return False
    else:
        return True

str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")
if(one_way(str1,str2)):
    print("edited")
else:
    print("diffrent text")
