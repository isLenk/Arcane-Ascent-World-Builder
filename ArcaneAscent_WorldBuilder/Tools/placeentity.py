from Tools.placing import PlacingTool
from pygame import Color
from filemanager import FileManager
from Generic.helperfuncs import *

class PlaceEntityTool(PlacingTool):
    hitboxSize = (3, 3)
    hitboxColor = Color(73, 186, 56)
    EntityLimit = 10
    CustomAttributes = {
        "Name": "Entity",
        "Resizable" : False,
        "Entity_Type": None
    }
    selectedEntity: Entity

    def generate(self):
        # content = "\njal LOAD_PICKUPS_MAP[LEVELNUM]:'\n"
        content = "LOAD_PICKUPS_MAP9:\n"
        content += FileManager.pushRA()
        content += 	"# Load Level Data\nla $a0, level_data\njal LOAD_DATA\n"
        childIDs, childNodes = self.get_children()
        currentOffsetAmt = 0
        for id in childIDs:
            child = childNodes[id]
            entityID = EntityCycler.get(child.Entity_Type).Name + "_ID"

            node = computeAreaAsRect(child.TopLeft, child.BottomRight)
            startPos = getAssemblyPos(node.topleft)
            content += "li $t0, {0}\n".format(int(startPos))
            content += "li $t1, {0}\n".format(entityID)
            content += "sw $t0, {0}(PICKUP_POINTER)\n".format(int(currentOffsetAmt*ENTITY_DATA_SIZE))
            content += "sw $t1, {0}(PICKUP_POINTER)\n".format(int(4+(currentOffsetAmt*ENTITY_DATA_SIZE)))

            currentOffsetAmt += 1
            if currentOffsetAmt > ENTITY_ARRAY_LIMIT: break
        
        if currentOffsetAmt > ENTITY_ARRAY_LIMIT: print(">> Too many entities on the Config.screen. Cut some off.")

        if currentOffsetAmt < ENTITY_ARRAY_LIMIT:   # Write cutoff
            content += "li $t0, 0\n"
            content += "sw $t0, {0}(PICKUP_POINTER)\n".format(int(currentOffsetAmt*ENTITY_DATA_SIZE))
            content += "sw $t0, {0}(PICKUP_POINTER)\n".format(int(4+(currentOffsetAmt*ENTITY_DATA_SIZE)))

        content += "la $a0, level_data\njal SAVE_DATA\n"
        content += FileManager.popRA()    
        return content.replace("\n", "\n\t") + "\n"
    
    def __init__(self):
        super().__init__()
        self.swapEntity()

    def swapEntity(self):
        self.selectedEntity = EntityCycler.getNext()
        self.hitboxColor = self.selectedEntity.Color
        self.hitboxSize = self.selectedEntity.Size
        self.CustomAttributes["Entity_Type"] = EntityCycler.get(self.selectedEntity.Name).Name

        print("Changing Entity to {0}".format(self.selectedEntity.Name))

    def processEvent(self, event):
        if event.type == pg.KEYUP:
            if event.key == KEYBINDS["CHANGE_ENTITY"]:
                self.swapEntity()
