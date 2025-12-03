class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head=node
        
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr= self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data)+ "-->"
            itr = itr.next
            
        print(llstr+"Null")

    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data, None)
            return

        itr=self.head

        while itr.next:
            itr=itr.next

        itr.next=Node(data, None)

    
    def insert_values(self, dlist):
        self.head = None
        for data in dlist:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self, position):
        if position<0 or position>self.get_length():
            raise Exception("Invalid Index")
        
        index=0

        itr=self.head

        while itr:
            if index == position -1:
                itr.next= itr.next.next
                break
            
            itr=itr.next
            index+=1

    def insert_at(self, position, data):
        if position<0 or position>self.get_length():
            raise Exception("Invalid Index")

        if position==0:
            self.insert_at_begining(data)
            return
        

        index=0

        itr=self.head

        while itr:
            if index ==position -1:
                node=Node(data, itr.next)
                itr.next=node

            itr=itr.next
            index+=1
    def insert_after(self, data_after, data_insert):
        itr=self.head
        flag=0
        
        while itr:
            if itr.data==data_after:
                node=Node(data_insert, itr.next)
                itr.next=node
                flag=1
                break
            itr=itr.next
        
        if flag==0:
            print("the element do not exist in the list")

    def remove_value(self, value):
        itr=self.head
        flag=0
        if itr is not None:
            while itr.next:
                if itr.next.data==value:
                    itr.next=itr.next.next
                    flag=1
                itr=itr.next
            
            if flag==0:
                print("the element do not exist in the list ")


    def reverse(self):
        current=self.head
        prev=None
        
        while(current):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
            
        self.print()
        
    def reverse_every_Kthelements(self, k):
        if not self.head or k==1:
            return self.headn
        l=self.get_length()
        newHead=Node(-1)
        newHead.next=self.head
        
        prev=newHead
        next =newHead
        curr=newHead
        
        while l>=k:
            curr=prev.next
            next=curr.next
            looop=l>k and k or l-1
            for i in range(1, looop):
                curr.next=next.next
                next.next=prev.next
                prev.next=next
                next=curr.next
            prev=curr
            l-=k
            
        self.head=newHead.next
        self.print()

ll = LinkedList()
ll.insert_values(["tiger", "fox", "dog", "cat", "rat"])
ll.remove_at(2)
ll.print()
ll.insert_at(2, "dog")
ll.insert_at_begining("dragon")
ll.print()
print(ll.get_length())
ll.insert_after("tiger", "lion")
ll.remove_value("dog")
ll.print()
ll.reverse()
ll.reverse_every_Kthelements(2)