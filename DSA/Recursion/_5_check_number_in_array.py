arr = [1,2,3,4,5,6,7,8,9]
num = 5

def chknum(arr,num):
    if len(arr)==0:
        return False
    if arr[0]==num:
        return True
    return chknum(arr[1:],num)

# print(chknum(arr,11))