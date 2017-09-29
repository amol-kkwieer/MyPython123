
def linear_search():
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [4, 2, 8, 9, 3, 7]

x = int(input("Enter the number to search: "))

ans = linear_search()

if ans == -1:
    print("%d is not in the array."%x)
else:
    print("%d is at %d position in array"%(x,ans+1))
