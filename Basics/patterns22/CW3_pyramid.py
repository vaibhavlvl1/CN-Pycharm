"""
to print the following pattern

    *
   ***
  *****
 *******

"""


n = int(input(""))

i = 1

while(i<=n):
    spaces=1
    while(spaces<=n-i):
        print(" ",end="")
        spaces=spaces+1


    stars=1
    while(stars<=i):
        print("*",end="")

        stars +=1


    stars=1
    while(stars<=i-1):
        print("*",end="")

        stars +=1

    print()
    i=i+1



"""
FOR LOOP solution
def function(n):
    for i in range(n):
        
        for j in range(n-i,1,-1):
            print("",end = " ")
        
        for j in range(i+1):
            print("*",end=' ')
            
        for k in range(i):
            print("*",end=" ")
            
        for k in range(n-i-1):
            print("",end=" ")
            
        print()
"""