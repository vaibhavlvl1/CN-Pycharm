
def sumofarray(arr):
    if len(arr)==1:
        return arr[0]
    return arr[0]+ sumofarray(arr[1:])

print(sumofarray([5,5,5,5,5,5,5,5,5,5]))