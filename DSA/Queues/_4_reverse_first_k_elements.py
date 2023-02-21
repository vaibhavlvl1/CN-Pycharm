# reverse first k elements of queue
import queue


def reverse1(q, k):
    if q.qsize() == 0 or k == 0:
        return

    x = q.get()

    reverse1(q, k - 1)

    q.put(x)


def reversek(q, k):
    reverse1(q, k)

    temp = q.qsize() - k
    while temp != 0:
        x = q.get()
        q.put(x)
        temp = temp - 1


q = queue.Queue()
n, k = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

for ele in arr:
    q.put(ele)

reversek(q, k)

while q.qsize() != 0:
    print(q.get(), end=" ")