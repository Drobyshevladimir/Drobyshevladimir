class  Box:
    def __init__ (self,cat = None):
        self.cat = cat
        self.nextcat = None
        self.previouscat = None

class Linkedlist:
    def __init__ (self):
        self.start = None
        self.len = 0

        
    def insertSomewhere(self,catIndex,newcat):
        
        if self.start is None and catIndex=1:
            newbox=Box(cat)
            self.start=newbox
            self.len=1
            
        else:
            if self.len+1<boxIndex:
                print('Error')
            else:
                newBox=Box(cat)
                boxIndex=0
                newbox.previouscat=None
                newbox.nextcat=self.start
                while boxIndex<=catIndex:
                    newbox=Box(cat)
                    a=newbox.previouscat
                    newbox.nextcat
            
        

        

        
