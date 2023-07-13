#recursive sum of digits of a number
def sum(n):
    if n == 0:
        return 0
    elif n < 0:
        print("Negative number")
    else:
        return n % 10 + sum(n // 10) 

try:
    n = int(input("Enter a number! "))
    res = sum(n)
    print("result =",res)
except ValueError:
    print("Enter integer number! ")   
    

        
    