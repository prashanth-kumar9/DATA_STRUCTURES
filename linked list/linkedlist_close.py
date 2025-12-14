class Node():
    def __init__(self, data=None, nxt=None):
        self.data=data
        self.nxt=nxt
class LinkedList:
    def __init__(self):
        self.head=None
    def getSize(self):
        size=0
        current=self.head
        while current:
            size+=1
            current=current.nxt   
        return size
    def insertElementatEnd(self, data):
        if self.head==None:
            node=Node(data)
            self.head=node
        else:
            current=self.head
            while(current.nxt):
                current=current.nxt
            
            node=Node(data)
            current.nxt=node
        
    def Displaylist(self):
            current=self.head
            while(current):
                print(str(current.data) + "-->", end="")
                current=current.nxt
            print("NULL")
    def insertdata(self, data):
        for  element in data:
            self.insertElementatEnd(element)
    def insertAt(self, position, data):
        if self.getSize()<position:
            return "the given position is not possible to add data"
        else:
            current=self.head
            count=0
            while count!=position-1:
                count+=1
                check=current
                current=current.nxt
            node=Node(data)
            check.nxt=node
            node.nxt=current
    def removeAt(self, position):
        if self.getSize()<position:
            return "the given position is not possible to add data"
        else:
            current=self.head
            count=0
            while count!=position-1:
                count+=1
                check=current
                current=current.nxt
            check.nxt=current.nxt
            
            
            
    def recursive_reverse(self, head) :
        if head is None or head.nxt is None:
            return head
        node=self.recursive_reverse(head.nxt)
        #print(str(node.data))
        #print(str(head.data))
        head.nxt.nxt=head
        #node.nxt=head
        head.nxt=None
        
        return node
        
        
        
            
        

ll = LinkedList()#
ll.insertdata(["tiger", "fox", "dog", "cat", "rat"])
ll.insertAt(2,"lion")
ll.removeAt(3)
ll2=LinkedList()
ll2.insertElementatEnd("fire")
#ll.remove_at(2)

ll.Displaylist()
print(ll.getSize())
ll2.Displaylist()
print(ll2.getSize())

ll.head=ll.recursive_reverse(ll.head)
print("after reverse")
ll.Displaylist()
