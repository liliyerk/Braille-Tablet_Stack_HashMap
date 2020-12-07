class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:

    def __init__(self):
        self.capacity = 52
        self.hashtable = [None] * self.capacity
        self.size = 0

    def hash(self, key):
        p = 71
        length = len(key)
        hash = 0
        for i in range(0, length):
            hash = hash + ord(key[i]) * p ** i
            i += 1
        hash = hash % self.capacity
        return hash

    def put(self, key, value):
        index = self.hash(key)
        if self.hashtable[index] == None:
            self.hashtable[index] = Entry(key, value)
            self.size += 1
            return None

        else:
            if self.hashtable[index].value != value:
                old_val = self.hashtable[index].value
                self.hashtable[index].value = value
                return old_val
            else:
                print("The key is already in the hashmap")

    def remove(self, key):
        index = self.hash(key)
        curr_item = self.hashtable[index]
        if curr_item.key == key:
            self.hashtable.remove(curr_item)

    def get(self, key):
        index = self.hash(key)
        if self.hashtable[index] != None:
            if self.hashtable[index].key == key:
                return self.hashtable[index].value

    def has_key(self, key):
        index = self.hash(key)
        if self.hashtable[index] != None:
            if self.hashtable[index].key == key:
                return True
        return False

    def has_value(self, value):
        for i in self.hashtable:
            if i != None:
                if i.value == value:
                    return True

        return False

    def print(self):
        print("Printing key value pairs!!!")
        for k in self.hashtable:
            if k != None:
                print(k.key + ": " + k.value)

    def import_from_json(self, my_dictionary):
        for k, v in my_dictionary.items():
            self.put(k, v)