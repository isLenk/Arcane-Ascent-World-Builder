import os
import pygame as pg
import Generic.config as Config
from Interfaces import Tool
from pathlib import Path

class ToolboxItem:
    Collection = list()
    iconDirectory = os.path.join(Path(__file__).parent.absolute(), 'icons')
    print(iconDirectory)
    icon: pg.Surface
    tool: Tool

    def __init__(self, iconName, tool):
        self.tool = tool
        self.icon = pg.image.load(os.path.join(self.iconDirectory, iconName))
        ToolboxItem.Collection.append(self)

    def get_icon(self): return self.icon
    def get_tool(self): return self.tool
