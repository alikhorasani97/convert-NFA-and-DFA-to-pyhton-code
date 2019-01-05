# ------------------------------------
# ------------------------------------
import copy



class Node:

    def __init__(self,namevalue):
        self.nameValue = namevalue
        self.nxtNode = {}
    def __copy__(self):
        return Node(copy.deepcopy(self.nameValue))
    def __repr__(self):
        return 'node ' + str(self.nameValue )


class stateMachine:
    """
    state machine that create from some nodes which connected whit edges
    """
    def __init__(self , headnode = None):
        if (type(headnode) is not Node):
            raise Exception("head must be as Node type")
        self.rootNode = copy.copy(headnode)
        self.Nodes = {}
        self.Nodes[str(self.rootNode.nameValue)] = self.rootNode
    def addNode(self,parentname,transformchar,newnamenode):
        newnode = Node(newnamenode)
        self.Nodes[str(newnamenode)] = newnode
        #print(list(self.Nodes[str(parentname)].nxtNode.keys))
        if(str(transformchar) in self.Nodes[str(parentname)].nxtNode):
            self.Nodes[str(parentname)].nxtNode[str(transformchar)].append(str(newnamenode))
        else:
            self.Nodes[str(parentname)].nxtNode[str(transformchar)] = [str(newnamenode)]

    def addEdge(self,parentname,transformchar,newnamenode):
        if((type(transformchar) is not str) or len(transformchar) != 1):
            raise Exception("transformchar must be string type whit lenght 1")# check to be a character for nfa and dfa
        if (transformchar in self.Nodes[str(parentname)].nxtNode):
            self.Nodes[str(parentname)].nxtNode[str(transformchar)].append(str(newnamenode))
        else:
            self.Nodes[str(parentname)].nxtNode[str(transformchar)] = [str(newnamenode)]


    def __copy__(self):
        return stateMachine(copy.copy(self.rootNode))

    def getRootNode(self):
        return self.rootNode




class problem:
    def __init__(self,stmchin):
        if (type(stmchin) is not stateMachine):
            raise Exception("input of problem must be stateMachine type")
        self.statemachine = copy.copy(stmchin)
        self.acceptNodes = [self.statemachine.Nodes[str(self.statemachine.rootNode.nameValue)]]

    def isInLanguage(self,string):
        if (type(string) is not str):
            raise Exception("input of isInLanguage function must be string type")
        for i in range(len(string)):
            if not (self.checkCharacter(string[i])):
                return False
        return True

    def checkCharacter(self,charctr):
        if ((type(charctr) is not str) or len(charctr) != 1):
            raise Exception("charctr must be string type whit lenght 1")  # check to be a character for nfa and dfa
        # curNode = self.acceptNodes.pop()
        tempnodes = copy.deepcopy(self.acceptNodes)
        self.acceptNodes[:] = []
        visitedNodes = []
        for node in tempnodes:
            if 'e' in node.nxtNode:
                for nxnode in node.nxtNode['e']:
                    if (self.statemachine.Nodes[str(nxnode)] in tempnodes) or (nxnode in visitedNodes) :
                        continue
                    tempnodes.append(self.statemachine.Nodes[str(nxnode)])
            if str(charctr) in node.nxtNode:
                for nxnode in node.nxtNode[str(charctr)]:
                    if self.statemachine.Nodes[str(nxnode)] in tempnodes:
                        continue
                    self.acceptNodes.append(self.statemachine.Nodes[str(nxnode)])
                visitedNodes.append(node.nameValue)
                tempnodes.pop()
        return bool(self.acceptNodes.__len__())




a = Node(5)
lklt=stateMachine(a)
language1=problem(lklt)
language1.statemachine.addNode(5,1,6)
language1.statemachine.addNode(6,0,7)
language1.statemachine.addNode(6,1,8)
language1.statemachine.addEdge(5,'1',8)
language1.statemachine.addEdge(5,'0',7)
print(a)
print(language1.isInLanguage('11'))
print(language1.acceptNodes)
