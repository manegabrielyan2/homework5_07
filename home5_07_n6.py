#recursive binary search
class NotFoundError(Exception):
    pass
def binary_search_recursive(array, target, low, high):
    try:
        target = float(target)
    except ValueError:
        raise ValueError("The input is not a number ")
    try:
        if low > high:
            return -1
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search_recursive(array , target , low , mid - 1)
        elif array[mid] < target:
            return binary_search_recursive(array , target , mid + 1 , high)
    except NotFoundError :
        raise NotFoundError("Target not found!")
    raise NotFoundError("Not found")
lst = [1 , 3 , 6 , 8]
key = 3
    
try:
    k = binary_search_recursive(lst , key , 0 , 3)
    print("Index of your target:" , k)
except ValueError as ve:
    print(str(ve))
except NotFoundError as n:
    print(str(n))
