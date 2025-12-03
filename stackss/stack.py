class Node():
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class Stack():
    def __init__(self):
        self.top=None
        
    def push(self, data):
        if self.top==None:
            self.top=Node(data, None)
        else:
            node = Node(data, self.top)
            self.top=node
    def isempty(self):
        if self.top==None:
            return True
        else:
            return False
    
    def pushexp(self, exp):
        for i in exp:
            self.push(i)
        
        
    def pop(self):
        if self.top==None:
            print("The stack is empty")
            return None
        else:
            t=self.top.data
            print("The deleted element is {}".format(self.top.data))
            self.top=self.top.next
            return t
        
    def get_length(self):
        index=0
        itr=self.top
        
        while itr:
            itr=itr.next
            index+=1
            
        return index
    
    def peek(self):
        t=self.top.data
        print("top of the stack is {}".format(t))
        return t
        
    def delete(self):
        while self.top:
            self.pop()
    
    def print_stack(self):
        itr=self.top
        stackstr=""
        while itr:
            stackstr+= str(itr.data)+"-->"
            itr=itr.next    
        print(stackstr)                
                    


