from stack import Stack as S

class Conversion:
    def __init__(self):
        self.postfix=None
        self.p={'+':1, '-':1, '*':2, '/':2, '^':3, '(':4}
        self.s=S()
        self.l=[]
    
    def infixtopostfix(self, exp):
        for i in exp:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "abcdefghijklmnopqrstuvwxyz":
                self.l.append(i)
            elif i=="(":
                self.s.push(i)
            elif i==")":
                while True:
                    ch=self.s.peek()
                    if ch=='(':
                        self.s.pop()
                        break
                    else:
                        self.l.append(self.s.top.data)
                        self.s.pop()
            else:
                while not self.s.isempty() and self.p[i]<=self.p[self.s.top.data]:
                    if self.s.top.data=="(":
                        break
                    else:
                        self.l.append(self.s.pop())
                self.s.push(i)
                    
        while self.s.top:
            self.l.append(self.s.pop())
        
        for i in self.l:
            print(i, end=" ")
        print("\n")

exp=input()
itp=Conversion()
itp.infixtopostfix(exp)