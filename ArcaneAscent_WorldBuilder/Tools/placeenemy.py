from Tools.placing import PlacingTool
from pygame import Color

class PlaceEnemyTool(PlacingTool):
    hitboxSize = (4, 5)
    hitboxColor = Color(158, 40, 40)
    EntityLimit = 10
    CustomAttributes = {
        "Name": "Enemy Spawn",
        "Resizable" : False
    }
