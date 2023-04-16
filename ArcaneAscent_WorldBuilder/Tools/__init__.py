from Interfaces import *
from Design.toolboxitem import ToolboxItem
from Generic.mapdata import MapData

from Tools.pen import PenTool
from Tools.placekey import PlaceKeyTool
from Tools.placeplayer import PlacePlayerTool
from Tools.placebrush import PlaceBrushTool
from Tools.placespike import PlaceSpikeTool
from Tools.placeentity import PlaceEntityTool
from Tools.resizecanvas import PlaceResizeCanvas
from Tools.placeenemy import PlaceEnemyTool
from Tools.placeexit import PlaceExitTool

mapData: MapData

def init():
    global mapData
    mapData = MapData.instance()

    
    # Create Toolbox Items
    tbiWall = ToolboxItem("Wall.png", PenTool())
    tbiKey = ToolboxItem("Key.png", PlaceKeyTool())   
    tbiExit = ToolboxItem("Exit.png", PlaceExitTool())
    tbiEnemy = ToolboxItem("EnemySpawn.png", PlaceEnemyTool())
    tbiPlayer = ToolboxItem("PlayerSpawn.png", PlacePlayerTool())
    tbiSpike = ToolboxItem("Spike.png", PlaceSpikeTool())
    tbiCoin = ToolboxItem("Coin.png", PlaceEntityTool())
    tbiBrush = ToolboxItem("PaintBrush.png", PlaceBrushTool())
    tbiResizeCanvas = ToolboxItem("ResizeCanvas.png", PlaceResizeCanvas())

    return tbiWall


newCanvasSizeFont = pg.font.SysFont('Helvetica', 20)
