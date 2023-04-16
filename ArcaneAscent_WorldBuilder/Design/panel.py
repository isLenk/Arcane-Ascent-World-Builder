from Interfaces import StaticDrawable
import pygame as pg
from constants import *
import Generic.config as Config

class Panel(StaticDrawable):
    _rect: pg.Rect
    name: str
    def __init__(self, rect):
        self._rect = rect
    
    def render(self, *args):
        pg.draw.rect(Config.screen, PanelBackgroundColor, self._rect)

    def setTop(self, y):
        self._rect.top = y
        
    def setBottom(self, y):
        self._rect.bottom = y

    def setHeight(self, h):
        self._rect.height = h
