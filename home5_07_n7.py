#bubble sort 
def bubble_sort(arr :list) -> list:
    try:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) ):
                if arr[i] > arr[j]:
                    arr[i] , arr[j] = arr[j] , arr[i]
        return arr        
    except TypeError:
        raise TypeError("You should enter numbers. ")
lst = [9 , -20 , - 20 , 45]
try:
    sorted = bubble_sort(lst)
    print(sorted)
except ValueError as ve:
    print(str(ve))
    
    
