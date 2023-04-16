from Interfaces import Events, Drawable
from Abstracts.singleton import Singleton
import pygame as pg
import Generic.config as Config
from constants import *

class Canvas(Events, Drawable, Singleton):
    isDragging = False

    @classmethod
    def init(self, canvas):
        self.surface = canvas
        self.dots_surface = pg.Surface(CANVAS_SIZE, pg.SRCALPHA)

        # Draw dots on Config.canvas
        for x in range(int(CANVAS_SIZE.x // 25) + 1):
            for y in range(int(CANVAS_SIZE.y // 25)+ 1):
                pg.draw.circle(self.dots_surface, CANVAS_DOTS, (x*25, y*25), 1)

    @property
    def surface(self): return self._surface

    @surface.setter
    def surface(self, canvasObject: pg.Surface):
        self._surface = canvasObject
    
    def onMouseMotion(self, *args):
        shiftAmt = args[0]
        if not self.isDragging: return
        Config.map_origin[0] += shiftAmt[0]
        Config.map_origin[1] += shiftAmt[1]

    def render(self, *args):
        # Draw the top left
        self.surface.blit(self.dots_surface, (5,5))
        # Iterate through Config.canvas' and place them onto map_base_canvas
        for canvasLayer in Config.map_layers:
            Config.map_base_canvas.blit(canvasLayer, (0,0))
        self.surface.blit(Config.map_base_canvas, Config.map_origin)
        self.surface.blit(Config.map_canvas_overlay, Config.map_origin)