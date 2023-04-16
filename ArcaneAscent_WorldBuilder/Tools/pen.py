from Interfaces import Tool
from Generic.helperfuncs import *
import Generic.config as Config
from Generic.nodeeditor import NodeEditor
from Generic.node import Node
from Generic.cursorhandler import CursorHandler

infoFont = pg.font.SysFont('Helvetica', 15)
class PenTool(Tool):
    isDragging = False
    awaitingDraw = False # Draw is Finished. Waiting to be collected
    def onMouseMotion(self, *args):
        if self.isDragging: return
        self.isDragging = self.isDragging == None and mapFocused(Config.mousePos)

    def onMouseUp(self, *args):
        if (self.isDragging or self.isDragging==None):
            self.awaitingDraw = True and mapFocused(Config.mousePos)
            self.isDragging = False

    def onMouseDown(self, *args):
        event = args[0]
        if event.button == 1 and not NodeEditor.get().Target:
            self.isDragging = None

    def render(self, *args): 
        # ? Hide cursor when over map.
        CursorHandler.setVisible(not mapFocused(Config.mousePos))
        
        # ? Show Drag Box
        if mapFocused(Config.mousePos) and self.isDragging and not NodeEditor.get().Target and Config.onMD_cell is not None:
            startRect = computeAreaAsRect(Config.onMD_cell, getCell(Config.mousePos))
            pg.draw.rect(Config.map_canvas, SEMI_OPAQUE, startRect)

        # ? Show indicators
        if (mapFocused(Config.mousePos)):
            currentCell = infoFont.render(str(getCell(Config.mousePos)), True, BLACK)
            Config.overlay.blit(currentCell, Vector2(Config.mousePos)+(15, 15)) 
            rect = getNode(Config.mousePos)
            yRect = rect.copy()
            xRect = rect.copy()

            xRect.left = 0
            xRect.width = Config.map_canvas.get_width()

            yRect.top = 0
            yRect.height = Config.map_canvas.get_height()

            pg.draw.rect(Config.map_canvas_overlay, Color(150,150,150), yRect)
            pg.draw.rect(Config.map_canvas_overlay, Color(150,150,150), xRect)
            pg.draw.rect(Config.map_canvas, MOUSE_OVER_NODE_COLOR, rect)

    def update(self, *args): 
        global onMD_cell
        # ------------------------------------------------------------------
        if (self.awaitingDraw and NodeEditor.get().HoveringOn is not None): self.awaitingDraw = False
        # ------------------------------------------------------------------
        
        # ? Create the new node.
        if (mapFocused(Config.mousePos) and self.awaitingDraw and Config.onMD_cell is not None and not NodeEditor.get().Target):
            self.awaitingDraw = False
            
            # * Add to node list.
            S, E = fixOrder(Config.onMD_cell, getCell(Config.mousePos))
            nodeSize = E-S
            if Config.restrict_min_flag == False or (nodeSize.x > 0 or nodeSize.y > 0):   # Build if larger than a pixel
                Node.addNode(Node(S, E , PLATFORM_COLOR))
                onMD_cell = None
