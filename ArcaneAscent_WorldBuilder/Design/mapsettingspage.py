from Interfaces import Page, StaticDrawable
from Design.textbox import Textbox
from constants import *
import pygame as pg
from Generic.helperfuncs import *
from Abstracts.singleton import Singleton

class MapSettingPage(Page, StaticDrawable): 
    name = "Map Settings"

    tbUnitSize: Textbox
    tbDisplayWidth: Textbox
    tbDisplayHeight: Textbox

    def Preload(absTopLeft):
        self = MapSettingPage
        surface:pg.Surface = self.surface
        tbWidth = surface.get_width() - 20
        self.tbUnitSize = Textbox(pg.Rect(0, 0, tbWidth, 40), surface, "Unit Size")
        self.tbDisplayWidth = Textbox(pg.Rect(0, 40, tbWidth, 40), surface, "Display Width")
        self.tbDisplayHeight = Textbox(pg.Rect(0, 80, tbWidth, 40), surface, "Display Height")
        self.tbUnitSize.setAbsTopLeft(absTopLeft)
        self.tbDisplayWidth.setAbsTopLeft(absTopLeft)
        self.tbDisplayHeight.setAbsTopLeft(absTopLeft)

        from Generic.mapdata import MapData
        self.mapData = MapData.instance()
        self.tbUnitSize.TextContent = str(MapData.get().unitSize)
        mapSize = self.mapData.getMapSize()
        self.tbDisplayWidth.TextContent = str(mapSize[0])
        self.tbDisplayHeight.TextContent = str(mapSize[1])

    def update(*args):
        self = MapSettingPage
        unitSizeChanged = MapSettingPage.tbUnitSize.TextChanged()
        displayWidthChanged = MapSettingPage.tbDisplayWidth.TextChanged()
        displayHeightChanged = MapSettingPage.tbDisplayHeight.TextChanged()
        if unitSizeChanged:
            self.mapData.unitSize = int(unitSizeChanged)
        if displayWidthChanged:
            self.mapData.displayWidth = int(displayWidthChanged)
        if displayHeightChanged:
            self.mapData.displayHeight = int(displayHeightChanged)
        
        if (unitSizeChanged or displayHeightChanged or displayWidthChanged):

            self.mapData.load(
                MapData.get().unitSize, 
                MapData.get().displayWidth, 
                MapData.get().displayHeight, 
                MapData.get().mapColor, 
                MapData.get().mapName
            )
            
            resizeMap()
            

    def render(*args):
        self = MapSettingPage
        surface:pg.Surface = self.surface
        surface.fill(EMPTY_COLOR)

        self.tbUnitSize.render(*args)
        self.tbDisplayWidth.render(*args)
        self.tbDisplayHeight.render(*args)
