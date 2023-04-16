from Tools.placing import PlacingTool
from Generic.helperfuncs import *
from filemanager import FileManager

class PlacePlayerTool(PlacingTool):
    hitboxSize = (4, 5)
    hitboxColor = Color(113, 146, 255)
    CustomAttributes = {
        "Name": "Player Spawn",
        "Resizable" : False
    }

    def generate(self):
        content = "PLACE_PLAYER_MAP9:\n"
        content += FileManager.pushRA()
        content += "la $a0, player_data\n"		# Load the player_data struct
        content += "jal LOAD_DATA\n"
        content += "li $t0, BASE_ADDRESS\n"

        childIDs, childNodes = self.get_children()
        for id in childIDs:
            child = childNodes[id]
            node = computeAreaAsRect(child.TopLeft, child.BottomRight)
            pos = getAssemblyPos(node.topleft)
            content += "addi $t0, $t0, {0}\n".format(int(pos))
            content += "move PLAYER_POS, $t0\n"
        content += "la $a0, player_data\n"		# Load the player_data struct
        content += "jal SAVE_DATA\n"
        content += FileManager.popRA()
        content = content.replace("\n", "\n\t")
        return content
