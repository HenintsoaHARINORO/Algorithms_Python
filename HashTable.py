class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size  # [None](a list) * 4 ->[None,None,None,None]
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))

                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] is None:  # set the new key
                    self.slots[nextslot] = key
                    self.data[nextslot] = data


                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size  # find the new slot

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] is not None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:  # otherwise continue going
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

h = HashTable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
print(h[1])
print(h[2])