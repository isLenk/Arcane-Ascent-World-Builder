from constants import *
import Generic.config as Config
from Abstracts.singleton import Singleton

class MapData(Singleton):
    Name = "MAP_DATA"
    mapName = "Map"
    unitSize: int
    displayWidth: int
    mapColor: list

    def getMapSize(self): return Vector2(self.displayWidth, self.displayHeight)

    def load(self, unitSize, displayWidth, displayHeight, mapColor = None, mapName = "Map"):
        self.mapName = mapName
        self.mapColor = mapColor
        Config.map_bg_color = mapColor
        self.unitSize = unitSize
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.copyUnitSize = unitSize
        self.copyDisplayWidth = displayWidth
        self.copyDisplayHeight = displayHeight
        Config.map_origin = CANVAS_SIZE/2 - (self.getMapSize())/2

    def reload(self):
        """Called on map load."""
        self.load(self.unitSize, 
                  self.displayWidth, 
                  self.displayHeight, 
                  self.mapColor, 
                  self.mapName)
        
    def init(self, unitSize, displayWidth, displayHeight, mapColor = Config.map_bg_color, mapName="Map"):
        self.load(unitSize, displayWidth, displayHeight, mapColor, mapName)
