#selection sort 
def selection_sort(arr : list) -> list:
    try:
        min = arr[0]
        index = 0 
        for i in range(len(arr)):
            for j in range( i + 1 , len(arr)):
                min = arr[i]
                index = i
                if arr[j] < min:
                    arr[i] = arr[j]
                    arr[j] = min
        return arr
    except TypeError:
        raise TypeError("You should enter numbers only. ")
lst = [6 , -90 , 44 , 3 , 25 , 44 ]
try:
    sorted = selection_sort(lst)
    print(sorted)
except TypeError as te:
    print('Type Error')
    print(str(te))