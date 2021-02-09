class Node():
    
    #Class that instantiates new node objects that contains a value left and right pointers.
    
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        
        #Some validation:
        if type(value) != int and type(value) != float:
            return False
        
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:   
            path = self.root
            
            #Looping to find the right node position for the value:
            while path != None:
                if path.value == newNode.value:
                    print(f'{newNode.value} already in the tree')
                    return None
                elif path.value < newNode.value:
                    if path.right == None:
                        path.right = newNode
                        print(f'Placed {newNode.value}to the right')
                        break
                    else:
                        print('Going to the right')
                        path = path.right
                    
                elif path.value > newNode.value:
                    if path.left == None:
                        path.left = newNode
                        print(f'Placed {newNode.value} to the left')
                        break
                    else:
                        path = path.left
                        print('Going to the left')
     
    def lookup(self,value):
        
        # Some validation:
        if type(value) != int and type(value) != float:
            return False
        if value == self.root.value:
            return self.root.value
        path = self.root
        
        # Looping until there is not a next node:
        while path !=None:
            if path.value == value:
                    print(f'{value} found.')
                    return path.value
                
            #Looking at the right
            elif path.value < value:
                    if path.right == None:
                        print(f'Value {value} not in the tree')
                        return False
                    else:
                        print('Searching to the right...')
                        path = path.right 
                        
            # Looking at the left            
            elif path.value > value:
                    if path.left == None:
                        print(f'Value {value} not in the tree')
                        return False
                    else:
                        path = path.left
                        print('Searching to the left...')            
            
               
    def remove(self,value):
        # This function deletes the node with he deleted node with minimum value node from the right subtree,
        # in the case of a node with 2 children
        
        
        # Validating inputs:
        if type(value) != int and type(value) != float:
            print('invalid value')
            return False
        if value == self.root.value and self.root.left == None and self.root.right == None:
            del self.root
            return None
        
        parentNode = self.root
        currentNode = self.root
        flag = ''
        
        while True:
            # When found the node with correspondent value we have 3 scenarios:
            # Node with no children, node with 1 child and node with 2 children
            # Each scenario is handled differently here:
            
            if currentNode.value == value:
                
                # No children
                if currentNode.left == None and currentNode.right == None:
                    print(f'Deleting {currentNode.value}')
                    if flag == 'right':
                        parentNode.right = None
                    else:
                        parentNode.left = None
                    break
                    
                # Only 1 child:     
                elif currentNode.left == None:
                    print(f'Deleting {currentNode.value}, naming {currentNode.right} as his successor')
                    currentNode.value = currentNode.right.value
                    currentNode.right = None
                    break
                elif currentNode.right == None:
                    print(f'Deleting {currentNode.value}, naming {currentNode.left} as his successor')
                    currentNode.value = currentNode.left.value
                    currentNode.left = None
                    break
                    
                # Node with two children:   
                else:
                    
                    #getting the minimum value node from the right subtree
                    pointer = currentNode
                    while pointer.left != None:
                        pointer = pointer.left
                    print(f'Replacing {currentNode.value} with {pointer.value}')    
                    currentNode.value = pointer.value
                    del pointer
                    break
                    
            # Trasversing throughout the Tree to find the right node:        
            else:
                if currentNode.value > value and currentNode.left == None:
                    print(f'{value} not in the tree')
                    break
                elif currentNode.value > value:
                    print('Moving to the left...')
                    parentNode = currentNode
                    currentNode = currentNode.left
                    flag = 'left'
                elif currentNode.value < value and currentNode.right == None:
                    print(f'{value} not in the tree')
                    break
                elif currentNode.value < value:
                    print('Moving to the right...')
                    parentNode = currentNode
                    currentNode = currentNode.right
                    flag = 'right'
                    
                    
                        
                    
        
