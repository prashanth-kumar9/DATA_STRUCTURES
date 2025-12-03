class Node():
    def __init__(self, data):
        self.data=data
        self.next=None
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Enqueue(self, data):
        if self.head==None:
            self.head=Node(data, None)
            self.tail=self.head
        else:
            node = Node(data, None)
            curr=self.head
            while(curr.next):
                curr=curr.next
            curr.next=node
            self.tail=curr.next
            
            
    def Enqueue_list(self, llist):
        #self.head=None
        for i in llist:
            self.Enqueue(i)
            
    def Dequeue(self):
        print(self.head.data)
        self.head=self.head.next
    
    def getLength(self):
        curr=self.head
        l=0
        while(curr):
            l+=1
            curr=curr.next
        return l
    
    def PrintQueue(self):
        curr=self.head
        queuestr=""
        while(curr):
            queuestr+=str(curr.data) + "-->"
            curr=curr.next
        print(queuestr)