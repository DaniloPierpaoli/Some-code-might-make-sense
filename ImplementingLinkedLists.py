class Node():
    
    #Class that instantiates new node objects that contains a value and a next pointer.
    
    def __init__(self,value):
        self.body = {'value': value,
         'next': None}

class Linked_List:
    
    # Class that implements Linked Lists Data Structures
    
    def __init__(self,value):
        
        self.head = Node(value).body
        self.tail = self.head
        self.length = 1
        
    def append(self,value):
        
        newNode = Node(value)
        #Creating a pointer
        self.tail['next'] = newNode.body
        self.length += 1
        #Update the reference
        self.tail = newNode.body
        
    def prepend(self, value):
        NewNode = Node(value)
        #Creating a pointer
        NewNode.body['next'] = self.head
        self.length += 1
        #Update the reference
        self.head = NewNode.body
            
    def insert(self,index,value):
        
        #Some insertion handling
        if index <= 0:
            return prepend(value)
        elif index >= self.length:
            return append(value)
        
        #Creating new node
        New_node = Node(value).body
        
        #Creating some reference
        current_node = self.head

        # Looping throughout the nodes
        Node_number = 1
        while Node_number < index:
    
            current_node = current_node['next']
            Node_number += 1
        
        # Creating reference to the tail at the index position, inserting the New node in that location
        # And ultimately assign the rest of the chain to the new_node pointer.
        to_tail_chain = current_node['next']
        current_node['next'] = New_node
        New_node['next'] = to_tail_chain
        
        self.length += 1
    
    def remove(self, index):
        
        if index <= 0:
            return self.remove_head()
        #Creating some reference
        current_node = self.head

        # Looping throughout the nodes
        Node_number = 0
        while Node_number < index-1:
    
            current_node = current_node['next']
            Node_number += 1
        
        
        
       
        node_to_delete = current_node['next']
        current_node['next'] = node_to_delete['next']
        
    
        
               
            
    def remove_head(self):
        self.head = self.head['next']
        
        
    def print_list(self):
        
        #Creating an array that contains all the values of the linked list
        
        array = []
        current_node = self.head
        while current_node['next'] != None:
            array.append(current_node['value'])
            current_node = current_node['next']
            if current_node['next'] == None:
                array.append(current_node['value'])
        print(array)    
            
        
        
