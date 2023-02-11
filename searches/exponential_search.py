def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0
 
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
 
    return _search(arr, i // 2, min(i, n), x)
 
 
def _search(arr, l, r, x):
    while r >= l:
        mid = l + (r - l) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
            r = mid - 1
 
        else:
            l = mid + 1
 
    return -1
 
 
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = exponential_search(arr, n, x)
 
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result)
