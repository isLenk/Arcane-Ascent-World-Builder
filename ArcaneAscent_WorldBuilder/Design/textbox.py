from Interfaces import Events, Drawable
from constants import *
import pygame as pg
import Generic.config as Config

propNameFont = pg.font.SysFont("Century Gothic", 11)
class Textbox(Events, Drawable):
    rect: pg.Rect
    surface: pg.Surface
    isFocused = False
    BackgroundColor = WHITE
    TextColor = BLACK
    TextContent = ""
    TemporaryTextContent = ""
    MarginHeight = 10
    propLabelWidth = 120
    FL_TEXT_CHANGED: bool = False # Assumes the handler will toggle this 

    # For integer only
    # TODO: Implement another class for specific textbox types
    intBoundary = [0, 0] # Default (0, 0) => no limit

    clearOnReturn = False
    acceptsOnlyInt = False

    def __init__(self,
                 relative_rect: pg.Rect,
                 surface: pg.Surface,
                 label: str):
        self.rect = relative_rect
        self.surface = surface
        self.absTopLeft = (0, 0)
        self.label = propNameFont.render(label, True, WHITE)
        from Generic.objecthandler import ObjectHandler
        ObjectHandler.addEventListener(self)
    
    def TextChanged(self):
        k = self.FL_TEXT_CHANGED
        self.FL_TEXT_CHANGED = False
        return k and self.TextContent or False
    
    def acceptOnlyInt(self, val: bool):
        self.acceptsOnlyInt = val

    def setAbsTopLeft(self, pos):
        self.absTopLeft = pos

    def render(self, *args):
        boundaryRect = self.rect.copy()
        boundaryRect.height -= self.MarginHeight
        boundaryRect.top += self.MarginHeight
        boundaryRect.width -= self.propLabelWidth
        boundaryRect.left += self.propLabelWidth
        pg.draw.rect(self.surface, self.BackgroundColor, boundaryRect)
        textValue = propNameFont.render(self.TextContent, True, self.TextColor)
        
        value_rect = textValue.get_rect(center=boundaryRect.center)
        label_rect = self.label.get_rect(midright = Vector2(boundaryRect.midleft) - (10, 0))
        self.surface.blit(textValue, value_rect)
        self.surface.blit(self.label, label_rect)#Vector2(boundaryRect.midleft) - (self.propLabelWidth, 0))

    def update(self, *args): pass

    def isHoveredOn(self):
        return self.rect.collidepoint(Vector2(Config.mousePos) - self.absTopLeft)
    
    def processEvent(self, event): 
        if event.type == pg.MOUSEBUTTONDOWN:
            # Check if hovering over self.
            if self.isHoveredOn() and event.button == 1:
                self.isFocused = True
                self.TemporaryTextContent = self.TextContent
            if self.isHoveredOn() and event.button == 3:
                self.isFocused = True
                self.TemporaryTextContent = self.TextContent
                self.TextContent = ""
        elif event.type == pg.MOUSEBUTTONUP:
            if not self.isHoveredOn() and event.button == 1:
                if self.isFocused:
                    self.isFocused = False

        if event.type == pg.KEYDOWN: 
            if not self.isFocused: return
            if event.key == pg.K_RETURN:
                print(self.TextContent)
                self.FL_TEXT_CHANGED = True
                if self.clearOnReturn:
                    self.TextContent = ''
            elif event.key == pg.K_BACKSPACE:
                self.TextContent = self.TextContent[:-1]
            elif event.key == pg.K_ESCAPE:
                self.TextContent = self.TemporaryTextContent
            else:
                # Check if value is numeric
                if self.acceptOnlyInt:
                 if (self.TextContent + event.unicode).isnumeric(): 
                    self.TextContent += event.unicode
                else:
                    self.TextContent += event.unicode
