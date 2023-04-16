from Interfaces import NodeProperties
import Generic.config as Config
from constants import BLACK

class Node(NodeProperties):
    id: int
    Collection = [] # Contains all of the nodes.
    Relations: list
    Layer: int = 0
    Deletable = True
    Color = BLACK

    def all(): return Node.Collection
    
    def addNode(node, relations=None): 
        Node.Collection.append(node)
        if relations is not None: node.Relations = relations

    def __init__(self, topLeft, bottomRight, color): 
        super().__init__()
        self.id = Config.currentNodeID
        Config.currentNodeID += 1
        self.Relations = None
        self.Color = color
        self.Layer = Config.current_canvas_layer
        self.setBounds(topLeft, bottomRight)
        #self.Collection.append(self)
    
    def setBounds(self, topLeft, bottomRight):
        self.TopLeft = topLeft
        self.BottomRight = bottomRight

    def delete(self):
        if type(self.Relations) is list:
            self.Relations.remove(self.id)
        Node.Collection.remove(self)
