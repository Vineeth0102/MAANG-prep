def union(arr1, arr2, size_arr1, size_arr2):
    uniqe_set = set(arr1 + arr2)
    return list(uniqe_set)

def union1(arr1, arr2, size_arr1, size_arr2):
    uni_map = {}
    for i in arr1:
        if i not in uni_map:
            uni_map[i] = True
    for i in arr2:
        if i not in uni_map:
            uni_map[i] = True
        
    uniq_list = []
    for i in uni_map.keys():
        uniq_list.append(i)
    return uniq_list
    
def union2(arr1, arr2, size_arr1, size_arr2):
    res = []
    arr1_counter = arr2_counter = 0
    if arr1[arr1_counter] < arr2[arr2_counter]:
        res.append(arr1[arr1_counter])
        arr1_counter += 1
    else:
        res.append(arr2[arr2_counter])
        arr2_counter += 1
    while(arr1_counter < size_arr1 and arr2_counter < size_arr2):
        if arr1[arr1_counter] < arr2[arr2_counter] and res[-1] == arr1[arr1_counter]:
            arr1_counter += 1
        elif arr1[arr1_counter] < arr2[arr2_counter]:
            res.append(arr1[arr1_counter])
            arr1_counter += 1
        elif arr1[arr1_counter] >= arr2[arr2_counter] and res[-1] == arr2[arr2_counter]:
            arr2_counter += 1
        elif arr1[arr1_counter] >= arr2[arr2_counter]:
            res.append(arr2[arr2_counter])
            arr2_counter += 1

    while(arr1_counter < size_arr1):
        if res[-1] != arr1[arr1_counter]:
            res.append(arr1[arr1_counter])
        arr1_counter += 1
    
    while(arr2_counter < size_arr2):
        if res[-1] != arr2[arr2_counter]:
            res.append(arr2[arr2_counter])
        arr2_counter += 1
    
    return res

size_arr1 = int(input("Enter the size of the Array1 : "))
arr1 = list(map(int, input("Enter Array1 elements: ").split()))
size_arr2 = int(input("Enter the size of the Array2 : "))
arr2 = list(map(int, input("Enter Array2 elements: ").split()))
print(union2(arr1, arr2, size_arr1, size_arr2))