import Generic.config as Config
from constants import *
from Generic.mapdata import MapData
import pygame as pg
import os
from Generic.mapdata import MapData

def getAssemblyPos(pos):
    x, y = pos
    return (y // MapData.get().unitSize) * (MapData.get().displayWidth//MapData.get().unitSize)*4 + (x // MapData.get().unitSize) * 4

def getAssemblyPosUsingIndex(pos):
    x, y = pos
    return y * (MapData.get().copyDisplayWidth//MapData.get().copyUnitSize) + (x // MapData.get().copyUnitSize) * 4

def pixel_expand(nodeData: list):
    node: Rect = computeAreaAsRect(nodeData.TopLeft, nodeData.BottomRight)
    data = ""
    startPos = getAssemblyPos( (node.topleft) )
    data += "addi $t0, $t0, {0}\n".format(startPos)
    for y in range( int(node.height//MapData.get().unitSize)):
        for x in range( int(node.width//MapData.get().unitSize)):
            data += "sw $t1, {0}($t0)\n".format(int(x*MapData.get().unitSize))
        data += "addi $t0, $t0, NEXT_ROW\n"
    return data

# Fills relative to position at $t0.
# For drawing static to map, use the following prior to call:
# content += "li $t0, BASE_ADDRESS\n"
def fill_expand(nodeData: list):
    data = ""

	# Position to the corner
    # Left term is its vertical height
    # Right term is its offset from the left
    startPos =  getAssemblyPosBINDEX( *(nodeData.TopLeft + Vector2(0,1)))
    data += "addi $t0, $t0, {0}\n".format(int(startPos))

    nodeWidth = (nodeData.BottomRight[0] - nodeData.TopLeft[0]) + 1
    nodeHeight = (nodeData.BottomRight[1] - nodeData.TopLeft[1]) + 1

    nodeEndPos = (nodeHeight - 1)*((MapData.get().copyDisplayWidth//MapData.get().copyUnitSize)*4) + (nodeWidth)*4
    # Store the start position
    data += "move $a0, $t0\n"
    # Shift $t0 to the end position
    data += "addi $t0, $t0, {0}\n".format(int(nodeEndPos))
    data += "move $a1, $t0\n"
    # Set row length to the width
    data += "li $a2, {0}\n".format(int(nodeWidth*4-4))
    data += "li $a3, {0}\n".format("WALL_COLOR")
    data += "jal FILL\n"
    return data

def resizeMap():
    global map_layers, map_base_canvas
    MapData.get().unitSize = MapData.get().copyUnitSize*Config.scale
    newWidth, newHeight = MapData.get().copyDisplayWidth*Config.scale, MapData.get().copyDisplayHeight*Config.scale

    newWidth -= newWidth%MapData.get().unitSize
    newHeight -= newHeight%MapData.get().unitSize

    MapData.get().displayWidth = newWidth
    MapData.get().displayHeight = newHeight

    Config.map_base_canvas = pg.transform.scale(Config.map_base_canvas, (newWidth, newHeight))
    for mapIndex in range(len(Config.map_layers)):
        Config.map_layers[mapIndex] = pg.transform.scale(Config.map_layers[mapIndex], (newWidth, newHeight))
    focusOnLayer(Config.current_canvas_layer, NO_NOTE=True)
    Config.map_canvas_overlay = pg.transform.scale(Config.map_canvas_overlay, (newWidth, newHeight))

def getNode(pos):
    rPos = posRelativeToMap(pos)
    focusedUnit = (rPos[0]//MapData.get().unitSize, rPos[1]//MapData.get().unitSize)
    rect = pg.Rect(focusedUnit[0]*MapData.get().unitSize, focusedUnit[1]*MapData.get().unitSize, MapData.get().unitSize, MapData.get().unitSize)
    return rect

def fixOrder(s, e):
    E = list(e)
    S = list(s)
    # Swap so that S always keeps top left most values.
    if (E[0] < S[0]): S[0], E[0] = E[0], S[0] 
    if (E[1] < S[1]): S[1], E[1] = E[1], S[1]

    return (Vector2(S), Vector2(E))

def computeAreaAsRect(s, e):
    S, E = fixOrder(s, e)

    rect = getNode(S)
    rect.left = (S[0])*MapData.get().unitSize
    rect.top = (S[1])*MapData.get().unitSize
    rect.width = (E[0] - S[0] + 1)*MapData.get().unitSize
    rect.height = (E[1] - S[1] + 1)*MapData.get().unitSize
    return rect

def computeOriginalAreaAsRect(s, e):
    S, E = fixOrder(s, e)

    rect = getNode(S)
    rect.left = (S[0])*MapData.get().copyUnitSize
    rect.top = (S[1])*MapData.get().copyUnitSize
    rect.width = (E[0] - S[0] + 1)*MapData.get().copyUnitSize
    rect.height = (E[1] - S[1] + 1)*MapData.get().copyUnitSize
    return rect

def getCell(position):
    """Return the a Vector2 cell index at "position" relative to map."""
    canvasPos = list(posRelativeToMap(position))
    cellPos = (
        canvasPos[0]//MapData.get().unitSize,
        canvasPos[1]//MapData.get().unitSize
    )
    return pg.Vector2(cellPos)

def posRelativeToMap(pos):
    return (pos[0] - CANVAS_TOPLEFT[0] - Config.map_origin[0],
             pos[1] - CANVAS_TOPLEFT[1] - Config.map_origin[1])

def posMapToAbs(mapPos):
    """Returns a vector of the absolute position 
    using the map-relative position "mapPos"
    """

    return (mapPos[0] + CANVAS_TOPLEFT[0] + Config.map_origin[0],
            mapPos[1] + CANVAS_TOPLEFT[1] + Config.map_origin[1])

def mipsRGBtoHex(r, g, b):
    return '0x00{:02x}{:02x}{:02x}'.format(r, g, b)

def getAssemblyPosBINDEX(x, y):
    return ((MapData.get().copyDisplayWidth // MapData.get().copyUnitSize ) * 4)*(y-1) + (x * 4)

def mapFocused(pos):
    rPos = posRelativeToMap(pos)
    if rPos[0] < 0 or rPos[1] < 0: return False
    if rPos[0] > MapData.get().displayWidth or rPos[1] > MapData.get().displayHeight: return False
    return True

def canvasFocused(pos):
    newPos = pg.Vector2(pos)
    newPos = newPos - CANVAS_TOPLEFT
    return newPos.x > 0 and newPos.y > 0 and newPos.x < CANVAS_SIZE[0] and newPos.y < CANVAS_SIZE[1]

def validateFile(fileToCheck):
    if fileToCheck.find(FILE_EXTENSION) < 0: fileToCheck += FILE_EXTENSION

    if not os.path.isfile(fileToCheck):
        print("File \"{0}\" provided does not exist.".format(fileToCheck))
        exit()
    return fileToCheck

def loadFile(fileToLoad):
    from filemanager import FileManager
    fileToLoad = validateFile(fileToLoad)
    FileManager.get().readMapFile(fileToLoad)
    print("Setting Current Opened File: {0}".format(fileToLoad))
    FileManager.get().current_opened_file = fileToLoad

def computeSizeAsRect(pos, dim):
    """ Returns a rect Config.canvas node positioned at "pos"
    with dimensions "dim"
    """
    rect = getNode(pos)
    rect.width = dim[0]*MapData.get().unitSize
    rect.height = dim[1]*MapData.get().unitSize
    return rect

def setLayerOpacities(layer):
     # Apply transparency to the Config.canvas layers.
     # The closer to the current layer, the more visible
    # Only works if layer opacities is enabled.
    for canvasIndex, canvasLayer in enumerate(Config.map_layers):  
        distanceFromCurrentLayer = abs(layer - canvasIndex)
        transparency = 255 - distanceFromCurrentLayer*LAYERING_OPACITY_CHANGE_BY_DISTANCE
        if Config.layering_opacity_enabled:
            canvasLayer.set_alpha(transparency)
        else: canvasLayer.set_alpha(255)

def focusOnLayer(layer, NO_NOTE = False):
    from Generic.nodeeditor import NodeEditor
    if layer != Config.current_canvas_layer: NodeEditor.get().setTarget(None)    # Deselect target as we are on new layer
    if not NO_NOTE: print(">> Modifying Layer {0}".format(layer+1))
    Config.current_canvas_layer = layer
    Config.map_canvas = Config.map_layers[Config.current_canvas_layer]
    setLayerOpacities(layer)
   
def selectTool(tool):
    if Config.can_change_tool == False: return
    if Config.ToolSelected:
        Config.ToolSelected.onToolDeselect()
    tool.onToolSelect()
    Config.ToolSelected = tool