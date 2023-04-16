from Tools.drag import DragTool
import pygame as pg
import Generic.config as Config
from constants import *
from Generic.helperfuncs import *
from Generic.mapdata import MapData
from Generic.nodeeditor import NodeEditor

infoFont = pg.font.SysFont('Helvetica', 15)
newCanvasSizeFont = pg.font.SysFont('Helvetica', 20)

# Unique functionality, allows dragging outside of Config.canvas
class PlaceResizeCanvas(DragTool):

    def __init__(self): # We do not want to add this to the collection
        self.rect = computeSizeAsRect((0,0), self.hitboxSize)
        self.children = list()

    def onToolSelect(self):
        self.isDragging = False
        self.awaitingDraw = False
        self.canvasCell_onMD = None
        self.canvasNode_onMD = None

    def onMouseMotion(self, *args):
        if self.isDragging: return
        self.isDragging = self.isDragging == None

    def onMouseUp(self, *args):
        if (self.isDragging or self.isDragging==None):
            self.awaitingDraw = True
            self.isDragging = False

    def onMouseDown(self, *args):
        event = args[0]
        if event.button != pg.BUTTON_LEFT: return
        if not self.rect: return
        if not self.canPlace: return
        self.isDragging = None
        self.canvasCell_onMD = getCell(Config.mousePos)
        self.canvasNode_onMD = getNode(Config.mousePos)

    def render(self, *args): 
        self.canPlace = (self.EntityLimit > len(self.children))
        # ? Hide cursor when over map.
        # CursorHandler.setVisible(not mapFocused(mousePos))
        
        # ? Show Drag Box
        if self.isDragging and not NodeEditor.get().Target and self.canvasCell_onMD is not None:
            endPos = getCell(Config.mousePos)
            startRect = computeAreaAsRect(self.canvasCell_onMD, endPos)
            startRect.topleft = CANVAS_TOPLEFT + Config.map_origin + self.canvasNode_onMD.topleft 
            pg.draw.rect(Config.overlay, SEMI_OPAQUE, startRect)
            # Display new Config.canvas size
            newSize = endPos - self.canvasCell_onMD
            newSizeLabel = newCanvasSizeFont.render("New Size ({0}, {1})".format(*newSize), True, WHITE)
            value_rect = newSizeLabel.get_rect(center=startRect.center)
            Config.overlay.blit(newSizeLabel, value_rect)
            
        # ? Show indicators
        currentCell = infoFont.render(str(getCell(Config.mousePos)), True, BLACK)
        Config.overlay.blit(currentCell, Vector2(Config.mousePos)+(15, 15)) 
        rect = getNode(Config.mousePos)
        rect.topleft += Vector2(CANVAS_TOPLEFT) + Config.map_origin

        yRect = rect.copy()
        xRect = rect.copy()

        xRect.left = 0
        xRect.width = Config.overlay.get_width()

        yRect.top = 0
        yRect.height = Config.overlay.get_height()

        pg.draw.rect(Config.overlay, Color(150,150,150), yRect)
        pg.draw.rect(Config.overlay, Color(150,150,150), xRect)
        pg.draw.rect(Config.overlay, MOUSE_OVER_NODE_COLOR, rect)

    def update(self, *args): 
        if not self.awaitingDraw or self.isDragging or self.canvasCell_onMD is None: return
        
        self.awaitingDraw = False
        self.isDragging = False
        endPos = getCell(Config.mousePos)
        startRect = computeAreaAsRect(self.canvasCell_onMD, endPos)
        startRect.topleft = CANVAS_TOPLEFT + Config.map_origin + self.canvasNode_onMD.topleft 
        newSize = endPos - self.canvasCell_onMD
        x, y = abs(newSize[0]), abs(newSize[1])
        MapData.get().load(MapData.get().unitSize, x*MapData.get().unitSize,
                           y*MapData.get().unitSize, MapData.get().mapColor, MapData.get().mapName)
        resizeMap()
        self.canvasCell_onMD = None