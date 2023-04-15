"""
to print following pattern

1        1
12      21
123    321
1234  4321
1234554321

"""

n = int(input())

i = 1

while(i<=n):

    j=1
    m=1

    while(j<=i):
        print(m,end="")

        m=m+1
        j=j+1

    spaces=1
    while(spaces<=n-i):
        print("  ",end="")
        spaces=spaces+1


    j=1
    h=i
    while(j<=i):
        print(h,end="")
        j=j+1
        h=h-1










    print()
    i=i+1



"""
def patten(n):
    for i in range(1,n+1):
        
        nums = 1
        for k in range(i):
            print(nums,end=" ")
            nums+=1
            
        for j in range(n-i,0,-1):
            print("0",end=" ")
        
        for l in range(n-i,0,-1):
            print("0",end=" ")
            
        nums2 = i
        for j in range(i):
            print(nums2,end=" ")
            nums2-=1
        print()
"""