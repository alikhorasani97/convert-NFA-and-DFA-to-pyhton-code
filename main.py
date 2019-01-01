# ------------------------------------
# ------------------------------------

class Node:

    def __init__(self,value):
        self.dataValue = value
        self.nxtNode = None

class linkList:
    def __init__(self , head):
        if(head == None):
            self.headList = None
        else:
            self.headList = head




class problem:
    def __init__(self,a = linkList()):
        self.head = a.headList

    #def checkCharacter(self):