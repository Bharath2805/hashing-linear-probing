class Dictionary:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def hashingFunction(self,key):
        return abs(hash(key))%self.size
    def rehash(self,oldHash):
        return (oldHash+1)%5
    def put(self,key,value):
        hashValue = self.hashingFunction(key)
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
        else:
            if self.slots[hashValue] == key :
                self.data = value
            else:
                newHashValue = self.rehash(hashValue)
        while self.slots[newHashValue] != None and self.slots[newHashValue] != key :
            newHashValue = self.rehash(newHashValue)
            if self.slots[newHashValue] == None:
                self.slots[newHashValue] = key
                self.data[newHashValue] = value
            else:
                self.data[newHashValue] = value 
        def __setitem__(self,key,value):
            self.put(key,value)


    def put(self,key):
        startPosition = self.hashingFunction(key)
        currentPosition = startPosition
        while self.slots[currentPosition] != None:
            if self.slots[currentPosition] == key :
                return self.data[currentPosition]
            currentPosition = self.rehash(currentPosition)
            if self.slots[currentPosition] == startPosition:
                return "NotFound"
        return "NotFound"
    def __getitem__(self,key):
        self.get(key)