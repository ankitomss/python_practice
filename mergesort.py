def mergeSort(num):
    n = len(num)
    if n == 1:
        return num
    elif n == 2:
        return [ min(num[0], num[1]), max(num[0], num[1])]

    left = mergeSort(num[:n/2])
    right = mergeSort(num[n/2:])

    ll, rr = 0, 0
    merge = []
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            merge.append(left[ll])
            ll += 1
        elif left[ll] > right[rr]:
            merge.append(right[rr])
            rr += 1
        else:
            merge.append(right[rr])
            merge.append(right[rr])
            ll += 1
            rr += 1

    while ll < len(left):
        merge.append(left[ll])
        ll += 1

    while rr < len(right):
        merge.append(right[rr])
        rr += 1

    return merge

num = [7,8,24,735,23,1,34,6,3]
print mergeSort(num)