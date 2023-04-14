def selection(li):
    print('정렬 전 : ', li)
    leng = len(li)
    for i in range(leng-1):
        for j in range(i+1, leng):
            if li[i]>li[j]:
                li[i], li[j] = li[j], li[i]
            print(f'{i}회전 : {li}')
    print('정렬 후 : ', li)


li = [5,4,3,1,2]
selection(li)
