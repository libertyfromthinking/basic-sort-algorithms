def merge(left, right):
    result = []
    while len(left)>0 or len(right)>0:
        if len(left)>0 and len(right)>0:
            if left[0]<=right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left)>0:
            result.append(left.pop(0))
        elif len(right)>0:
            result.append(right.pop(0))
    return result


def merge_sort(li):
    if len(li)<=1:
        return li
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

l = [6,5,4,3,2,1]
print(merge_sort(l))
