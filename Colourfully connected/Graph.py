# numNodes = 100
# edges=[]

# class Node:
#     def __init__(self,id,x,y):
#         self.id=id
#         self.position =[x,y]
#         self.connections=int(random(0,numNodes))
#         self.connectedTo=[]
#         for i in range(self.connections):
#             node = -1
#             while node==-1 or node not in self.connectedTo:
#                 node = int(random(0,self.connections))
#                 self.connectedTo.append(node)
#         edges.append(self.connectedTo)
                
                
#         def drawEdges()
                
        
class Node:
    def __init__(self, node_id, position):
        self.id = node_id
        self.connectedTo = []
        self.position = position

    def add_connection(self, node_id):
        self.connectedTo.append(node_id)
