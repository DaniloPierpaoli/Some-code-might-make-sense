'''
This class uses OOP to create an object that has the properties of Array Data Structure:
push() method, pop() method, delete, insert and search.

'''

class Array():
    
    def __init__(self):
        self.data = {}
        self.length = 0
        
        
    def getValue(index):
        
        return self.data[index]
    
    def pop(self):
        
        item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return item
    
    
    def push(self,item):
        
        self.data[self.length] = item
        self.length +=1
        
        
    def delete(self,index):
        
        self.data[index] = None
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1] 
        self.length -= 1
        
        
    def insert(self,item,index):
        
        self.push(self.data[self.length-1])
        for i in range(index+1,self.length-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item 
        
        
    def search(self,item):
        
        for i in range(0,self.length-1):
            if self.data[i] == item:
                return (item,i)
        
        
            
        
