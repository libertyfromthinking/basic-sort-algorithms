li = [4,3,1,2]

def bubble(li):
    le = len(li)
    for i in range(1,le):
        for j in range(i-1,-1,-1):
            if li[j]>li[j+1]:
                li[j+1], li[j] = li[j], li[j+1]
            else:
                break

bubble(li)
print(li)
