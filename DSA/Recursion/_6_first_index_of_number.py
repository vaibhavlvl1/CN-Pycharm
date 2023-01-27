"""

"""

def first_index(arr,n,index=0):
    if len(arr)==0:
        return -1
    if arr[0]==n:
        return index

    return first_index(arr[1:],n,index+1)

arr= [0,1,2,3,4,5,6,7]

print(first_index(arr,7))
