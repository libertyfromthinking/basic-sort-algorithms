def binary_search(li, item):
    left = 0
    right = len(li)-1
    while left<=right:
        mid = (left+right)//2
        if mid == item:
            return mid
        else:
            if mid>item:
                right = mid-1
            else:
                left = mid+1

li = [1,2,3,4,5,6,7,8,9,10,11]

print(binary_search(li, 3))

