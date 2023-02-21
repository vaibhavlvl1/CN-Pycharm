
from sys import stdin

def stockSpan(x, n) :
    s = []
    for i in range(len(x)-1,0,-1):
        #print(x[i])
        c = 1
        for j in range(i-1,-1,-1):
            if x[i]>x[j]:
                c=c+1
            else:
                break
        s.append(c)
    s.append(1)
    return s[::-1]


































'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
