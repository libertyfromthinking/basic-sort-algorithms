def shell(li):
    if len(li)<2:
        return li
    
    gap = len(li)//2
    print(gap)
    while gap>0:
        for i in range(len(li)):
            insert_gap(li, gap, i)
        gap //= 2
        print(gap)
    return li

def insert_gap(li, gap, start):
    for i in range(start, len(li), gap):
        value = li[i]
        index = i
        while index>start and value<li[index-gap]:
            print(f'index : {index}')
            li[index] = li[index-gap]
            index -= gap
        li[index] = value

print(shell([3,2,5,4,1,6]))
