def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    
    left = []
    right = []
    
    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quick_sort(left) + [pivot] + quick_sort(right)

arr = [19, 7, 15, 12, 16, 18, 4, 11, 13]
print(quick_sort(arr))