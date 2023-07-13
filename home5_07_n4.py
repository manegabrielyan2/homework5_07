#binary search iterative
class NotFoundError(Exception):
    pass
def binary_search(iterable , key):
    try:
        key = float(key)
    except ValueError:
        raise ValueError("Target is not a number")

    try:
        start = 0
        end = len(iterable) - 1
        while start <= end :
            middle = (start + end) // 2
            if key == iterable[middle]:
                return middle
            elif key < iterable[middle]:
                end = middle - 1
            else :
                start = middle + 1
        raise NotFoundError("Target not found. ")
    except NotFoundError :
        raise NotFoundError("Target not found!!! ")

lst = [1 , 2, 3 , 4 , 5]
key = 'n'
try :
    
    index = binary_search(lst , key)
    print("Index of target is " , index )
except NotFoundError as m:
    print(str(m))
    
except ValueError as er:
    print(str(er))
    


