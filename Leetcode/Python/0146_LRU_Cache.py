'''
146. Design a data structure that follows the constraints of a Least 
Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size 
capacity.
int get(int key) Return the value of the key if the key exists, 
otherwise return -1.
void put(int key, int value) Update the value of the key if the
 key exists. Otherwise, add the key-value pair to the cache. If 
 the number of keys exceeds the capacity from this operation, 
 evict the least recently used key.
 
The functions get and put must each run in O(1) average time
 complexity.
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        if self.capacity == len(self.cache):
            del self.cache[next(iter(self.cache))]         
        self.cache[key] = value

lRUCache = LRUCache(2)
print(lRUCache.put(1, 1)) 
print(lRUCache.put(2, 2)) # cache is {1=1, 2=2}
print(lRUCache.get(1))  #// return 1
print(lRUCache.put(3, 3)) #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))   #// returns -1 (not found)
print(lRUCache.put(4, 4)) #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))   #// return -1 (not found)
print(lRUCache.get(3))   #// return 3
print(lRUCache.get(4))   #// return 4
 