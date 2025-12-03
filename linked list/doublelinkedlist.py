class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev=prev
        self.data=data
        self.next=next

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self, data):
        node=Node(None, data, self.head)
        self.head=node
            
    def insert_at_end(self, data):
        
        if self.head is None:
            self.head=Node(None, data, None)
            return
        
        itr=self.head
        
        while itr.next:
            itr=itr.next
            
        itr.next=Node(itr, data, None)
    
    def insert_at(self, position, data):
        if position<0 or position>dll.get_length():
            raise Exception("Invalid Index")
        
        if position==0:
            self.insert_at_begining(data)
            return
        
        itr=self.head
        index=0
        while itr:
            if index==position-1:
                node=Node(itr, data, itr.next)
                if node.next:
                    node.next.prev=node
                itr.next=node
                break
            itr=itr.next
            index+=1
    def remove_at(self, position):
        if position<0 or position>self.get_length():
            raise Exception("Invalid Index")
            return

        itr=self.head
        index=0
        while itr:
            if index==position-1:
                itr.next=itr.next.next
                itr.next.prev=itr
            itr=itr.next
            index+=1
        
        
    def printforward(self):
        if self.head is None:
            print("The List is empty")
            return
        itr=self.head
        dllstr=""
        
        while itr:
            dllstr+="<--"+str(itr.data)+"-->"
            itr=itr.next
        print(dllstr)
        
    def printbackward(self):
        if self.head is None:
            print("The List is empty")
            return
        itr=self.get_last_Node()
        dllstr=""
        while itr:
            dllstr+="<--"+str(itr.data)+"-->"
            itr=itr.prev
        print(dllstr)
            
    def insert_values(self, datalist):
        self.head=None
        
        for data in datalist:
            self.insert_at_end(data)
    
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
            
        return count
    
    def get_last_Node(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr





dll=DoubleLinkedList()

dll.insert_values(["PineApple", "Grapes", "Oranges"])
dll.insert_at(2, "Mango")
print(dll.get_length())
dll.remove_at(1)
dll.printbackward()
dll.printforward()
print(dll.get_last_Node().data)