#insertion sort

def insertion_sort(arr):
    try:
        if (n := len(arr)) <= 1:
            return
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr    
    except TypeError:
        raise TypeError("You should enter only numbers. ")
lst = [5 , 4 , 3 , 2 , 1]
try:
     new = insertion_sort(lst)
     print(new)
except TypeError as te:
    print(str(te))
