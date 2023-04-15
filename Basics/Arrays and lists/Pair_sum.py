# finally my own solution

def pair_sum(li, K):

    res = []
    i = 0
    numpairs = 0

    for i in range(n):

        for j in range(i + 1, n):

            if li[i] + li[j] == K:
                numpairs += 1

    return numpairs


t = int(input())
while (t != 0):
    n = int(input())
    if n == 0:
        print("0")
        break

    li = [int(x) for x in input().split()]

    K = int(input())

    h = pair_sum(li, K)

    print(h)

    t = t - 1


"""
def pairSum(arr,target):
    count = 0
    d = {}
    
    for i in arr:
        if target - i in d:
            count = count + d[target-i]
        
        d[i]=d.get(i,0)+1
    
            
        
            
    return count
"""

"""
for indivi pairs

def pairsum(arr,k):
    li = []
    d = {}
    count = 0
    for ele in arr:
        if k - ele in d:
            count = count+d[k-ele]
            li.append((k-ele,ele))
        d[ele] = d.get(ele,0)+1
            
    return li
"""