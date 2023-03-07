class MapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None


class Map:
    def __init__(self):
        self.bucket_size = 10
        self.buckets = [None for i in range(self.bucket_size)]
        self.count = 0

    def size(self):
        return self.count

    def get_index(self,hc):
        return hc%self.bucket_size

    def insert(self,key,value):
        hc = hash(key)
        index = abs(get_index)

        head = self.buckets[index]

        node = MapNode(key,value)
        node.next = head
        self.buckets[index] = node
        self.count +=1
