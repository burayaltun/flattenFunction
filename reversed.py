def reversed_list1 (array1):
    for i in range(len(array1)):
        if type(array1[i]) == type([]):
            array1[i] = array1[i][::-1]
            reversed_list1(array1[i])
    
    return (array1[::-1])

array1 = [1,2,[3,4,5],[6,7,[8,9,10]],11,12]
print(reversed_list1(array1))