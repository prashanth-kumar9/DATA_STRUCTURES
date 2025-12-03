from stack import Stack as S

class Palindrome:
    
    def __init__(self):
        self.s=S()
        self.tempS=S()
        
    def checks(self, exp):
        for i in exp:
            self.s.push(i)
        
        l=self.s.get_length()
        
        if l%2==0:
            for i in range(l//2):
                self.tempS.push(self.s.peek())
                self.s.pop()
        else:
            for i in range(l//2):
                self.tempS.push(self.s.peek())
                self.s.pop()
            self.s.pop()
        
        for i in range(l//2):
            if self.tempS.peek()==self.s.peek():
                self.s.pop()
                self.tempS.pop()
            else:
                break
        if self.s.isempty():
            return print("Palindrome")
        else:
            return print("Not Palindrome")

palindrome="abcaba"
p=Palindrome()
p.checks(palindrome)