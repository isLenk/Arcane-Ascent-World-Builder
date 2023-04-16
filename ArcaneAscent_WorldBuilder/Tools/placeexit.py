from Tools.placing import PlacingTool
from Generic.helperfuncs import *

class PlaceExitTool(PlacingTool):
    hitboxSize = (7, 8)
    hitboxColor = Color(56, 56, 56)
    EntityLimit = 1
    CustomAttributes = {
        "Name": "Exit Point",
        "Resizable" : False
    }
    # ! TODO: IMPLEMENT SPRITE LOADER VERSION
    def generate(self):
        content = "PLACE_EXIT:"
        childIDs, childNodes = self.get_children()
        for id in childIDs:
            child = childNodes[id]
            
            node = computeAreaAsRect(child.TopLeft, child.BottomRight)
            startPos = getAssemblyPos(node.topleft)

            content = "Instructions: Place in 'LOAD_LEVEL_DATA_[LEVELNUM]:'\n"
            content += "li GATE_POSITION, {0}\n\n\n".format(int(startPos))
        return content
