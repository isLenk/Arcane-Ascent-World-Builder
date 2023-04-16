from Tools.placing import PlacingTool
from Generic.helperfuncs import *

class PlaceKeyTool(PlacingTool):
    hitboxSize = (6, 2)
    hitboxColor = Color(255, 224, 112)
    EntityLimit = 3
    CustomAttributes = {
        "Name": "Gate Key",
        "Resizable" : False
    }
    def generate(self):
        content = "\nInstructions: Place in 'LOAD_LEVEL_DATA_[LEVELNUM]:'\n"
        childIDs, childNodes = self.get_children()
        for id in childIDs:
            child = childNodes[id]
            node = computeAreaAsRect(child.TopLeft, child.BottomRight)
            startPos = getAssemblyPos(node.topleft)

            content += "li KEY_POSITION, {0}\n".format(int(startPos))
        
        return content
