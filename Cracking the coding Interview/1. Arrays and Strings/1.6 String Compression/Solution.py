def string_compression(orginal_value):
    count = 1
    new_val = ''
    for i in range(len(orginal_value)-1):
        if orginal_value[i] == orginal_value[i+1]:
            count += 1
        else:
            new_val = new_val+ orginal_value[i] + str(count)
            count = 1
    new_val = new_val+ orginal_value[i+1] + str(count)
    if len(new_val) > len(orginal_value):
        return orginal_value
    else:
        return new_val



val = "test" #input("Enter the String : ")
print(string_compression(orginal_value=val))
