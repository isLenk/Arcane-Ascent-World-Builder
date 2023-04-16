import Generic.config as Config
import pygame as pg
from Interfaces import Tool
from constants import *
from Generic.helperfuncs import *
from Generic.nodeeditor import NodeEditor
from Generic.node import Node
from Generic.cursorhandler import CursorHandler
    
# ? Use to update tool entity counters on LOADED_NEW_MAP
class PlacingTool(Tool):
    isDragging = False
    canPlace = True
    rect: pg.Rect
    hitboxSize = (2,2)
    hitboxColor = BLACK

    CustomAttributes:dict
    EntityLimit = 1
    children: list = list()
    NOT_SAVED = {
        "children": dict()
    }
    
    def __init__(self):
        Config.placing_tool_collection.append(self)
        self.rect = computeSizeAsRect((0,0), self.hitboxSize)
        self.children = list()
        self.NOT_SAVED = PlacingTool.NOT_SAVED.copy()

    def get_children(self):
        return (self.children, self.NOT_SAVED["children"])
    
    def generate(self): 
        """Returns a content string when generating"""
        return ""

    def applyAttributes(self, node: Node):
        node.loadProperties(self.CustomAttributes.copy())

    def onMouseMotion(self, *args): 
        if not mapFocused(Config.mousePos) or not self.rect: return
        newPos = getNode(Config.mousePos)
        self.rect.left = newPos[0]
        self.rect.top = newPos[1]
 
    def onMouseUp(self, *args): pass

    def onMouseDown(self, *args):
        from Generic.nodeeditor import NodeEditor
        if NodeEditor.get().HoveringOn: return
        event = args[0]
        if event.button != pg.BUTTON_LEFT: return

        if not mapFocused(Config.mousePos) or not self.rect: return
        if not self.canPlace: return
        absPos = posMapToAbs(self.rect.topleft)
        absBottomPos = posMapToAbs(self.rect.bottomright)
        child = Node(getCell(absPos), getCell(absPos) + self.hitboxSize - (1, 1), self.hitboxColor)
        Node.addNode(child, self.children)
        # TODO: Make this better
        if self.children.__contains__(child.id):
            newID = Node.id
            Node.id += 1
            print("Conflicting ID (ID:{0}). Repositioning to end (ID:{1})".format(child.id, newID))
            child.id = newID
        self.children.append(child.id)
        self.NOT_SAVED["children"][child.id] = child
        self.applyAttributes(child)
        
    def render(self, *args):  
        if not mapFocused(Config.mousePos) or not self.rect: return

        # Draw hologram rect is not placed
        if self.canPlace: pg.draw.rect(Config.map_canvas_overlay, self.hitboxColor, self.rect)

    def update(self, *args):  
        self.canPlace = (self.EntityLimit > len(self.children))
        CursorHandler.setVisible(True)
        if (mapFocused(Config.mousePos)):
            newDims = computeSizeAsRect(Config.mousePos, self.hitboxSize)
            self.rect.size = newDims.size
            CursorHandler.setCursor(pg.SYSTEM_CURSOR_HAND)
        else:
            CursorHandler.setCursor(pg.SYSTEM_CURSOR_ARROW)
