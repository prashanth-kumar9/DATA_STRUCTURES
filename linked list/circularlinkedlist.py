from pickle import TRUE


class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev=prev
        self.data=data
        self.next=next

class CircularLinkedList():
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self, data):
        node=Node(None, data, self.head)
        itr= self.head

        if self.head is not None:
         while(itr.next != self.head):
            itr = itr.next
         itr.next = node
         node.prev=itr
        else:
         node.next = node
        self.head=node
    
    def insert_at_end(self, data):
        
        node=Node(None, data, self.head)
        if self.head is not None:
            itr=self.head
            while itr.next!=self.head:
                itr=itr.next
                
            itr.next=node
            node.prev=itr
            return
        else:
            node.next=node
            self.head=node
            return
            
            

    def insert_values(self, datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)
            
    def get_length(self):
        count=0
        itr=self.head
        
        if self.head is None:
            return count
        else:
            count+=1
            while itr.next!=self.head:
                count+=1
                itr=itr.next
            
        return count
    
    def insert_at_position(self, pos, data):
        if pos < self.get_length():
            node=Node(None, data, None)
            itr=self.head
            count=0
            while True:
                count+=1
                
                if count==pos-1:
                    node.next=itr.next
                    itr.next=node
                    node.prev=itr
                    
                itr=itr.next
                if itr==self.head:
                    break
        
    def remove_at_position(self, pos):
        
        if pos<0 or pos> self.get_length():
            raise Exception("Invalid Index")
            return
        itr=self.head
        count=0
        while itr:
            count+=1
            if pos-1 == count:
                itr.next=itr.next.next
                itr.next.prev=itr
                
            itr=itr.next
            if itr==self.head:
                break
                    
                
            
    
    def printforward(self):
         itr=self.head
         cllstr=""
         if self.head is None:
            print("List is Empty")
            return
        
         else:
            while TRUE:
                cllstr+="<--"+str(itr.data)+"-->"
                itr=itr.next
                if itr==self.head:
                    break
            
         print(cllstr)
            

cll=CircularLinkedList()
cll.insert_at_begining(34)
cll.insert_at_begining(54)
cll.insert_values(["pen", "pencil", "ink", "paper", "paint"])
cll.insert_at_position(3, "sketches")
cll.printforward()
print(cll.get_length())
cll.remove_at_position(3)
cll.printforward()
print(cll.get_length())