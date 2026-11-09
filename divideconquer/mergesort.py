def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left,right)
    
def merge(left, right):
    nL, nR = len(left), len(right)
    i = j = 0
    result = []
    while i < nL and j < nR:
        if left[i] <= right[j]:     
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    if i < nL:
        result.extend(left[i:])
    if j < nR:
        result.extend(right[j:])
    return result

arr = [6, 5, 12, 10, 9, 1]
print(mergeSort(arr))