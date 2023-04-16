from Interfaces import Events, Drawable
from Abstracts.singleton import Singleton
from Generic.helperfuncs import *
from Generic.cursorhandler import CursorHandler
from copy import deepcopy


class NodeEditor(Singleton, Events, Drawable):
    HoveringOn          = None
    Target              = None       
    storedValues        = None
    isResizing          = False
    isOverResizeButton  = False 
    isMouseDown         = False

    def onMouseMotion(self, *args):
        if self.isResizing and mapFocused(Config.mousePos) and \
            (hasattr(self.Target, "Resizable") and getattr(self.Target, "Resizable") or 
             not hasattr(self.Target, "Resizable")):
            S, E = fixOrder(list(self.Target.TopLeft), getCell(Config.mousePos))
            self.Target.TopLeft, self.Target.BottomRight = S, E

        if self.isMouseDown and self.Target and self.HoveringOn:
            CursorHandler.setVisible(True)
            CursorHandler.setCursor(pg.SYSTEM_CURSOR_HAND)
            # Shift by displacement from mouse down
            displacement = Config.onMD_cell
            displacement = getCell(Config.mousePos) - displacement
            self.Target.setBounds(
                self.storedValues.TopLeft + displacement,
                self.storedValues.BottomRight + displacement)

    def onMouseDown(self, *args):
        event = args[0]
        if event.button != pg.BUTTON_LEFT: return
        if self.isOverResizeButton:
            self.isResizing = True
        else:
            if self.Target and not self.isResizing:
                self.isMouseDown = True

    def setTarget(self, target):
        from Design.propertypage import PropertyPage
        self.Target = target
        PropertyPage.Target = target
        self.storedValues = deepcopy(target)

    def update(self, *args):
        if self.isResizing:
            CursorHandler.setVisible(True)
            CursorHandler.setCursor(pg.SYSTEM_CURSOR_SIZENWSE)

    def render(self, *args):
        map_canvas, nodeColor, rect = args

        # Deselect
        if K_RETURN in Config.keySelected:
            self.setTarget(None)

        color = addColor(nodeColor, (30, 30, 60))
        pg.draw.rect(map_canvas, color, rect)

        # Draw Resize
        if hasattr(self.Target, "Resizable") and getattr(self.Target, "Resizable") != False or not hasattr(self.Target, "Resizable"):
            
            circleRadius = max(5, min(rect.width, rect.height)//30)
            circleColor = NODE_EDIT_RESIZE_COLOR
            Target_Resize = pg.Rect(rect.right-circleRadius/2, rect.bottom-circleRadius/2, circleRadius+2, circleRadius+2)

            if Target_Resize.collidepoint(posRelativeToMap(Config.mousePos)):
                circleColor = addColor(circleColor, 50)
                self.isOverResizeButton = True
            pg.draw.circle(map_canvas, circleColor, rect.bottomright, circleRadius, 2)
