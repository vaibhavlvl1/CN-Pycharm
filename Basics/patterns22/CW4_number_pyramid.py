"""
to print following pattern
   1
  232
 34543
4567654

"""


n = int(input())

i = 1
x=2
while(i<=n):

    spaces=1
    while(spaces<=n-i):
        print(" ",end="")
        spaces=spaces+1
    d=i
    j=1
    while(j<=i):
        print(d,end="")
        j+=1
        d+=1

    j=1


    x= 2*i-2
    while(j<=i-1):
        print(x,end="")
        x-=1
        j +=1






    print()
    i +=1


"""
using for loops

def num_pyramid(n):
    nums2 = 2
    for i in range(1,n+1):
        
        # space
        for space in range(n-i):
            print(" ",end=" ")
            space = space+1
        
        # nums
        nums1 = i
        for j in range(1,i+1):
            print(nums1,end = " ")
            nums1+=1
        
        p = 2*i-2
        for k in range(1,i):
            print(p,end=" ")
            p = p-1

        print()
"""