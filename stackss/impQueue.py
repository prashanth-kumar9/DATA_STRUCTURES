class Queueustack():
    def __init__(self, stack1=None, stack2=None):
        self.stack1=[]
        self.stack2=[]
    def enqu(self,x):
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
            
        self.stack1.append(x)
        
        while len(self.stack2)!=0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
            
    def dequ(self):
        if len(self.stack1)==0:
            return 0
        else:
            x=self.stack1[-1]
            self.stack1.pop()
            return x
        
queue1=Queueustack()
queue1.enqu(1)
queue1.enqu(2)

print(queue1.dequ())
print(queue1.dequ())
print(queue1.dequ())