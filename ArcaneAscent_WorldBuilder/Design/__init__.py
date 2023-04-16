import pygame as pg
from constants import *
from Design.twopanel import TwoPanel
from Design.propertypage import PropertyPage
from Design.mapsettingspage import MapSettingPage
from Design.toolboxpage import ToolboxPage
from Design.filespage import FilesPage
from Generic.objecthandler import ObjectHandler

if not pg.font.get_init(): pg.font.init()

propsAndMaps = TwoPanel(PropertyPage, MapSettingPage)
propsAndMaps.setHeight(300)
propsAndMaps.setBottom(CANVAS_TOPLEFT[1] + CANVAS_SIZE[1])

toolsAndFiles = TwoPanel(ToolboxPage, FilesPage)
toolsAndFiles.setHeight(300)
toolsAndFiles.setLeftSideHeight(280)
toolsAndFiles.setBottom(propsAndMaps._rect.top - PADDING)

propsAndMaps.generatePageSurfaces()
toolsAndFiles.generatePageSurfaces()
ObjectHandler.add(toolsAndFiles)
ObjectHandler.add(propsAndMaps)
