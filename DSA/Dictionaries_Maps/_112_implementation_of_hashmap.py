class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.bucket_size = 10
        self.buckets = [None for i in range(self.bucket_size)]
        self.count = 0

    def get_size(self):
        return self.count

    def __get_index(self, hc):
        return abs(hc % self.bucket_size)

    def loadfactor(self):
        return self.count / self.bucket_size

    def rehash(self):
        old_buckets = self.buckets
        self.bucket_size = self.bucket_size * 2
        self.buckets = [None for i in range(self.bucket_size)]
        self.count = 0

        for head in old_buckets:
            while head is not None:
                self.insert(head.key, head.value)

                head = head.next

    def insert(self, key, value):
        hc = hash(key)
        index = self.__get_index(hc)

        head = self.buckets[index]
        while head is not None:
            if key == head.key:
                head.value = value
                return
            head = head.next

        head = self.buckets[index]
        newNode = MapNode(key, value)
        newNode.next = head
        self.buckets[index] = newNode
        self.count += 1

        if self.loadfactor() >= 0.7:
            self.rehash()

    def remove(self, key):
        hc = hash(key)
        index = self.__get_index(hc)

        head = self.buckets[index]
        prev = None
        while head is not None:
            if head.key == key:
                if prev is None:
                    self.buckets[index] = head.next
                    self.count -= 1
                    return
                else:
                    prev.next = head.next
                    self.count -= 1
                    return
            prev = head
            head = head.next
        return None