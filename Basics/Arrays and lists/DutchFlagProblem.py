#sort any number list

li = [ 1,1,0,0,1,1,0,0,2,2,2,2,1,1,0]


for i in range (len(li)):

    for j in range (i+1,len(li)):

        if li[i]>li[j]:
            li[i],li[j] = li[j],li[i]
            print(li)

print(li)


"""
single scan solution

def sort012(arr):
    l = 0
    r = len(arr)-1
    m = 0
    
    while m <= r:
        if arr[m] == 1:
            m = m+1
        elif arr[m] ==0:
            arr[l],arr[m] = arr[m],arr[l]
            l = l+1
            m = m+1
        else:
            arr[m],arr[r] = arr[r],arr[m]
            r = r-1
        
    
"""