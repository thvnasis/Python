#this script is made to make exponential search using the binary search too which is created inside this script too


#here we create the exponential_search function which takes as input a list of integers and an integer to search
#in this function we perform an exponential search to find an upper bound for the binary search 
def exponential_search(list, x):
    if list[0] == x:
        return 0
    i = 1
    while i < len(list) and list[i] <= x:
        i *= 2
    lower = i // 2
    upper = min(i, len(list) - 1)
    return binary_search(list, x, lower, upper)#we return the list,the integer and the uppper and lower bounds for the binary search    

    
def binary_search(list, x, lower, upper):
    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] < x:
            lower = mid + 1
        elif list[mid] > x:
            upper = mid - 1
        else:
            return mid
    return -1  # Not found
    
#the binary search here is performed between the range that is given by the above-mentioned exponential search
