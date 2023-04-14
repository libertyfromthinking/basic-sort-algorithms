def insertion(li):
    print('정렬 전 : ',li)
    leng = len(li)
    for i in range(1,leng):
        for j in range(i-1, -1, -1):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
            else:
                break
    print('정렬 후 : ',li)

li = [5,4,3,2,1]
insertion(li)
