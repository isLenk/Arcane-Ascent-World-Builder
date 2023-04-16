from Interfaces import StaticDrawable
from Interfaces import Page
from constants import *
import pygame as pg
from Abstracts.singleton import Singleton
from Generic.nodeeditor import NodeEditor
from Generic.cursorhandler import CursorHandler
import Generic.config as Config
import re

propNameFont = pg.font.SysFont("Century Gothic", 11)
class PropertyPage(Page, StaticDrawable): 
    yOffset = 0
    propertyNameSpace = 80
    propertyRowHeight = 40
    rowSpacing = 3
    name = "Properties"
    Target = None
    HoveringOn = None

    def loadProperties(target): PropertyPage.Target = target

    def render(*args):
        global currCursorIcon
        absTopLeft = args[0]
        self = PropertyPage
        surface:pg.Surface = self.surface
        surface.fill( EMPTY_COLOR) #ToolboxPage.ListBackgroundColor)

        if not self.Target: return

        if self.HoveringOn: self.HoveringOn = None

        # Get property data
        for i, prop in enumerate(NodeEditor.get().Target.getProps().keys()):
            name = prop
            if not hasattr(NodeEditor.get().Target, name): return
            value = getattr(NodeEditor.get().Target, name)
            readableName = " ".join(re.split('(?<=.)(?=[A-Z])', name))
            yPos = i*(self.propertyRowHeight+self.rowSpacing)
            boundingRect = pg.Rect(0, yPos, surface.get_width(), self.propertyRowHeight)

            propNameLabel   = propNameFont.render(readableName, True, WHITE)
            propValueLabel  = propNameFont.render(str(value), True, WHITE)

            valueRect = boundingRect.copy()
            valueRect.left = 5 + self.propertyNameSpace
            valueRect.width -= 5 + self.propertyNameSpace
            valueRect.height -= 10
            valueRect.top += 5

            surface.blit(propNameLabel, (5, yPos + self.propertyRowHeight/2 - propNameFont.size(readableName)[1]/2))
            pg.draw.rect(surface, PanelSecondaryColor, valueRect, border_radius=3)
            surface.blit(propValueLabel, (10 + self.propertyNameSpace, yPos + self.propertyRowHeight/2 - propNameFont.size(str(value))[1]/2))

            if valueRect.collidepoint(Config.mousePos - absTopLeft):
                self.HoveringOn = prop
                CursorHandler.setCursor(pg.SYSTEM_CURSOR_IBEAM)

        if not self.HoveringOn:
             CursorHandler.setCursor(pg.SYSTEM_CURSOR_ARROW)
