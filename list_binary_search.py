def list_binary_search(list,value):
    if len(list)<=1:
        if value ==list[0]:
            return True
        return False
    else:     
        if value<list[len(list)//2]:
            new_list=list[:len(list)//2]
        else:
            new_list=list[len(list)//2:]
        return list_binary_search(new_list,value)

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
print list_binary_search(A,0)
print list_binary_search(A,1)
print list_binary_search(A,2)
print list_binary_search(A,13)
print list_binary_search(A,24)
print list_binary_search(A,25)
print list_binary_search(A,26)
