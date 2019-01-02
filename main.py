# ------------------------------------
# ------------------------------------
import copy



class Node:

    def __init__(self,namevalue):
        self.nameValue = namevalue
        self.nxtNode = {}
    def __copy__(self):
        return Node(copy.deepcopy(self.nameValue))


class linkList:
    def __init__(self , headnode = None):
        if (type(headnode) is not Node):
            raise Exception("head must be as Node type")
        self.headName = str(headnode.nameValue)
        self.Nodes = {}
        self.Nodes[self.headName] = copy.copy(headnode)

    def addNode(self,parentname,transformchar,newnamenode):
        newnode = Node(newnamenode)
        self.Nodes[str(newnamenode)] = newnode
        if(transformchar in self.Nodes[str(parentname)].nxtNode):
            self.Nodes[str(parentname)].nxtNode[str(transformchar)].append(str(newnamenode))
        else:
            self.Nodes[str(parentname)].nxtNode[str(transformchar)] = [str(newnamenode)]

    def addEdge(self,parentname,transformchar,newnamenode):
        if (transformchar in self.Nodes[str(parentname)].nxtNode):
            self.Nodes[str(parentname)].nxtNode[str(transformchar)].append(str(newnamenode))
        else:
            self.Nodes[str(parentname)].nxtNode[str(transformchar)] = [str(newnamenode)]


    def __copy__(self):
        return linkList(copy.copy(self.headNode))

    def getheadlist(self):
        return self.headList




class problem:
    def __init__(self,lnkList):
        if (type(lnkList) is not linkList()):
            raise Exception("input of problem must be linkList type")
        self.linklist = copy.copy(lnkList)
        self.acceptNodes = [self.linklist.Nodes[str(self.linklist.headName)]]

    def isInLanguage(self,string):
        if (type(lnkList) is not str()):
            raise Exception("input of isInLanguage function must be string type")


    def checkCharacter(self,charctr):
        while(True):
            curNode=self.acceptNodes.pop()


a = Node(5)
lklt=linkList(a)
lklt.addNode(5,1,6)
print(lklt.Nodes[str(a.nameValue)].nxtNode)
