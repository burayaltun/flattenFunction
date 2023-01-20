list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten_list1 = [] 

def flatten (x,y):
    for i in x:
        if type(i) != type([]):
            y.append(i)
        elif type(i) == type([]):
            flatten(i,y)
    return y

print(flatten(list1, flatten_list1))


