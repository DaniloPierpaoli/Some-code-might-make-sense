import random

class Hash_table():
    
    # The goal of this class is creating a brand new hash table data structure
    # We store data within the array assuming we don't have hash table available.
    # Hash function simply generates pseudo-random integers from 0 to data size from a given key.
    
    
    def __init__(self, size):
        self.size = size
        self.data = [None]*size
    
    def _hash_(self, key):
    
        random.seed(key)
        return random.randint(0,self.size-1)
    
    def Set(self,key,value):
        
        index = self._hash_(key)
        
        # Managing collisions:
        if self.data[index] == None:
            self.data[index] = [None]
            self.data[index][0] = [key,value]
        else:
            self.data[index].append([key,value])
            
        
    def Get(self, key):
        
        # Retrieve the index from the _hash_ function:
        go_address = self.data[self._hash_(key)]
        
        # Checking for collisions
        if len(go_address) == 1:
            return self.data[self._hash_(key)][0][1]
        
        # Retrieving values that use the same key from a collision:
        else:
            values = []
            for item in go_address:
                if item[0] == key:
                    values.append(item[1])
            return values        
                    
    
    def Delete(self,key):
        
        #Deleting keys and values
        go_address = self.data[self._hash_(key)]
        i = 0
        for item in go_address:
            if item[0] == key:
                del self.data[self._hash_(key)][i]
            i += 1    
                
                
    def Keys(self):
        #Retreiving all keys
        keys_array = []
        
        for data_block in self.data:
            if data_block != None:
                
                #Loop through the potential collision
                for values in data_block:
                    if values[0] not in keys_array:
                        keys_array.append(values[0])
                        
        return keys_array          
           
