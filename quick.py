def quick(li):
    if len(li)<=1:
        return li
    pivot = li[0]
    greater = [element for element in li[1:] if element>pivot]
    lesser = [element for element in li[1:] if element<=pivot]
    return quick(lesser) +[pivot]+ quick(greater)

li = [5,4,3,2,1]
print(quick(li))
