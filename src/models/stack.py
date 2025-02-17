class Stack:
    def __init__(self): #initialsising empty list
        self.item=[]
    def push(self,data):  #pushing elements into the stack
        self.item.append(data)    
    def pop(self):    #poping elements from the stack
        self.item.pop()
    def is_empty(self):  #checking the elements inside the stack
        if len(self.item)==0:
            return True
        else:
            return False
                