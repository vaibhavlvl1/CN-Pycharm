"""

"""

def last_index(arr,n,index=-1,end_index=0):
    if len(arr)==0:
        return index
    if arr[0]==n:
        index = end_index
    return last_index(arr[1:],n,index,end_index+1)


arr=[1,2,3,4,5,2,1,0]
print(last_index(arr,2))