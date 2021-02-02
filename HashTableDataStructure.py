import random

class Hash_table():
    
    # The goal of this class is creating a brand new hash table data structure
    # We store data within the array assuming we don't have hash table avaiable.
    # Hash function simply generates pseudo-random integers from 0 to 50 from a given key.
    
    
    def __init__(self, size):
        self.size = size
        self.data = [None]*size
    
    def _hash_(self, key):
    
        random.seed(key)
        return random.randint(0,self.size)
    
    def Set(self,key,value):
        index = self._hash_(key)
        self.data[index] = [key,value]
        
    def Get(self, key):
        # Retrieve the index from the _hash_ function:
        return self.data[self._hash_(key)][1]
