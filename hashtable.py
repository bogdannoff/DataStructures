import hashlib


class LinkedList:

    class LinkedListNode:

        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None

        def __str__(self):
            return f'[{self.key}:{self.val}]'

    def __init__(self):
        self.head = None

    def __str__(self):
        s = []
        el = self.head
        while el:
            s.append(str(el))
            el = el.next
        return ' -> '.join(s)

    def insert(self, key, val):
        new_el = LinkedList.LinkedListNode(key, val)
        new_el.next, self.head = self.head, new_el

    def get(self, key):
        el = self.head
        while el:
            if el.key == key:
                return el.val
            el = el.next
        return None

    def remove(self, key):
        el = self.head
        el_perv = None
        while el:
            if el.key == key:
                if el_perv is None:
                    self.head = el.next
                else:
                    el_perv.next = el.next
                val = el.val
                del el
                return val
            el_perv = el
            el = el.next
        return None


class HashTable:

    def __init__(self, size, hashf):
        self.length = 0
        self.size = size
        self.table = [None] * size
        self.hashf = hashf

    def __str__(self):
        s = []
        for el in self.table:
            s.append(str(el))
        return '\n'.join(s)

    def _get_hash_index(self, key):
        #return int(self.hashf(str(key).encode()).hexdigest(), 16) % self.size
        return self.hashf(key) % self.size

    def insert(self, key, val):
        idx = self._get_hash_index(key)
        if self.table[idx] is None:
            self.table[idx] = LinkedList()
        self.table[idx].insert(key, val)

    def get(self, key):
        idx = self._get_hash_index(key)
        if self.table[idx] is not None:
            return self.table[idx].get(key)
        return None

    def remove(self, key):
        idx = self._get_hash_index(key)
        if self.table[idx] is not None:
            return self.table[idx].remove(key)
        return None



ht = HashTable(20, hashlib.md5)
ht = HashTable(2, lambda x: int(hashlib.md5(str(x).encode()).hexdigest(), 16))
ht.insert('1', 'awdrgdqxerg')
ht.insert('8', 20)
ht.insert('10', 10)
ht.insert('3', 'yyy')
print(ht)


ht.remove('3')
print(ht)


nums = [1,2,3,4]

for i,x in enumerate(nums[1::]):
    nums[i+1] += nums[i]

print(nums)