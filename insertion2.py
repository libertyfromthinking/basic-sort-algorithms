def insertion(li):
    print('정렬 전 : ', li)
    for i in range(1,len(li)):
        j = i-1
        key = li[i]
        while li[j]>key and j>=0:
            li[j+1] = li[j]
            j = j-1
        li[j+1] = key
    print('정렬 후 : ', li)

li = [5,4,3,2,1]
insertion(li)
