
def bubbleSort(li):
    print('정렬 전 : ', li)
    leng = len(li)-1
    for i in range(leng):
        for j in range(leng-i):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    print('정렬 후 : ', li)


li = [5,4,2,3,1]

bubbleSort(li)
