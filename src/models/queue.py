class Queue:
    def __init__(self):
        self.item=[]
        print("you re in queue class")
     
     
    def Enqueue(self,data):
            self.item.append(data)
    
    def Dequeue(self):
        self.item.pop(0)        
        
    def is_empty(self):
        if len(self.item)==0:
            return True 
        else:
            return False   