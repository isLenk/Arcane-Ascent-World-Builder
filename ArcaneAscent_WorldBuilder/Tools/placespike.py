from Tools.drag import DragTool
from filemanager import FileManager
from Generic.mapdata import MapData
from pygame import Color
from Generic.helperfuncs import *


class PlaceSpikeTool(DragTool):
    hitboxSize = (4,2)
    fixedSizeY = 2
    hitboxColor = Color(100, 100, 100)
    EntityLimit = 32
    CustomAttributes = {
        "Name": "Spike",
        "Resizable" : False
    }

    def generate(self):    
        content = "LOAD_SPIKES_MAP9:\n"
        content += FileManager.pushRA()
        childIDs, childNodes = self.get_children()
        for id in childIDs:
            content += "li $t0, BASE_ADDRESS\n"
            child = childNodes[id]
            node = computeAreaAsRect(child.TopLeft, child.BottomRight)
            startPos = getAssemblyPos(node.topleft)

            content += "addi $t0, $t0, {0}\n".format(int(startPos))
            # nodeHeight = node.height//mapData.unitSize
            # nodeWidth = node.width//mapData.unitSize

            nodeWidth = (child.BottomRight[0] - child.TopLeft[0])
            nodeHeight = (child.BottomRight[1] - child.TopLeft[1]) 

            nodeEndPos = (nodeHeight)*((MapData.get().copyDisplayWidth//MapData.get().copyUnitSize)*4) + nodeWidth*4

            # Store the start position
            content += "move $a0, $t0\n"
            # Shift $t0 to the end position
            content += "addi $t0, $t0, {0}\n".format(int(nodeEndPos))
            content += "move $a1, $t0\n"
            # Set row length to the width
            content += "li $a2, {0}\n".format(int(nodeWidth*4))
            content += "jal DRAW_SPIKES\n"
        content += FileManager.popRA()
        content = content.replace("\n", "\n\t")
        return content
