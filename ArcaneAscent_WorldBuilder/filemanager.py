import os
import json
import Generic.config as Config
from Generic.mapdata import MapData
from constants import *
import pygame as pg
from Generic.helperfuncs import *
from Generic.node import Node
from Abstracts.singleton import Singleton

class FileManager(Singleton):
    workspacePath: str
    spritesFolder: str
    mapsFolder: str
    generatedFolder: str
    current_opened_file: str
    
    def init(self):
        self.current_opened_file = None
        self.workspacePath = os.path.join(Config.directory_path,"workspace")
        self.spritesFolder = os.path.join(self.workspacePath, "sprites")
        self.mapsFolder    = os.path.join(self.workspacePath, "maps")
        self.generatedFolder    = os.path.join(self.workspacePath, "generated")

        def createIfMissing(path):
            # Create workspace directory
            if not os.path.isdir(path):
                print("Path does not exist.")
                print("Creating directory ({0})".format(path))
                os.mkdir(path)
            else:
                print("Directory ({0}) found".format(path))
        createIfMissing(self.workspacePath)
        createIfMissing(self.spritesFolder)
        createIfMissing(self.mapsFolder)
        createIfMissing(self.generatedFolder)
        
    def saveMapFile(self, outName, data):
        raw_content = list()
        
        # Save map data
        mapDataCopy = MapData.get().__dict__
        mapDataCopy["Name"] = MapData.Name
        mapDataCopy["displayWidth"] = MapData.get().copyDisplayWidth
        mapDataCopy["displayHeight"] = MapData.get().copyDisplayHeight
        mapDataCopy["unitSize"] = MapData.get().copyUnitSize
        mapDataCopy["mapColor"] = list(Config.map_bg_color)

        raw_content.append(mapDataCopy)
        
        print("Saving Map Data:")
        print("- Dimensions ({0}, {1})\n - Unit Size ({2})".format(
            MapData.get().copyDisplayWidth,
            MapData.get().copyDisplayHeight,
            MapData.get().copyUnitSize))
        print("- Map Color: RGB{0}".format(Config.map_bg_color))
        saveTracker = {}
        for index, node in enumerate(data):
            name = "Wall"
            if hasattr(node,"Name"): name = getattr(node, "Name")

            # Keep track of how many of each node type was saved
            # TODO: Don't one line this.
            saveTracker[name] = 0 if not saveTracker.__contains__(name) \
                else saveTracker[name] + 1

            # print(index, "({0})".format(name and name or "Wall"), node)

            save_content = node.__dict__

            # Degrade non-JSON serializable objects
            for k, v in node.__dict__.items():
                if type(v) is Vector2:
                    save_content[k] = list(v)
                elif type(v) is Color:
                    save_content[k] = list(v)
                elif k == "NOT_SAVED": # Do not save.
                    save_content[k] = None
            raw_content.append(save_content)
        json_object = json.dumps(raw_content, indent=4)

        outputPath = self.current_opened_file or os.path.join(self.mapsFolder, outName+FILE_EXTENSION)
        with open(outputPath, "w") as outfile:
            outfile.write(json_object)
        # Display the results
        for k, v in saveTracker.items(): print("+ {0}({1})".format(k, v))

    def pushRA(): return "# Push return address to stack.\naddi	$sp, $sp, -4\nsw	$ra, 0($sp)\n"
    def popRA(): return "# Return to sender.\nlw	$ra, 0($sp)\naddi	$sp, $sp, 4\njr	$ra\n"

    def generateMap(self, nodes):
        out_path = os.path.join(self.generatedFolder, "map_generated.asm")
        f = open(out_path, "w")

        content = "DRAW_MAP9:\n"
        content += FileManager.pushRA()

        content += "jal PLACE_PLAYER_MAP9\njal LOAD_SPIKES_MAP9\njal LOAD_PICKUPS_MAP9\n"
        content += "li $t1, WALL_COLOR\n"
        specialNodes = []
        wallsPlaced = 0

        for tool in Config.placing_tool_collection:
            specialNodes += tool.children

        specialNodeCount = 0
        if DRAWING_METHOD == "PIXEL":
            for node in nodes:
                
                if node in specialNodes: 
                    specialNodeCount += 1
                    continue
                content += "li $t0, BASE_ADDRESS\n"
                data = pixel_expand(node)
                content+=data
                wallsPlaced += 1
        elif DRAWING_METHOD == "FILL":
            for node in nodes:
                if node.id in specialNodes: 
                    specialNodeCount += 1
                    continue
                content += "li $t0, BASE_ADDRESS\n"
                data = fill_expand(node)
                content += data
                wallsPlaced += 1

        print("Ignored {0} special nodes".format(specialNodeCount))
        # Add Jump Back
        content += FileManager.popRA()
        # Indent Everything
        content = content.replace("\n", "\n\t")
        f.write(content)
        f.close()
        print("Finished Map Generation. Placed {0} walls".format(wallsPlaced))

    def generateEntity(self, nodes):
        out_path = os.path.join(self.generatedFolder, "entity_generated.asm")
        f = open(out_path, "w")
        content = ""

        numEntities = 0
        for tool in Config.placing_tool_collection:     
            print("Generating {0}...".format(tool.CustomAttributes["Name"]))
            numEntities += len(tool.children)
            content += tool.generate()
            content += "\n\n"
            print("-" * 15)

        f.write(content)
        f.close()
        print("Finished Entity Generation. Placed {0} entities".format(numEntities))
        
    def generate(self, nodes):
        self.generateMap(nodes)
        self.generateEntity(nodes)

    # ! Requires Rework
    def generateRelative(self, nodes):
        numEntities = 0
        out_path = os.path.join(self.mapsFolder, "relative_entity_generated.txt")
        f = open(out_path, "w")
        # content = "move $t9, $a0\n"
        for node in nodes:
            # content += "move $t0, $t9\n"
            data = pixel_expand(node)
            content += data
            numEntities += 1
        f.write(content)
        f.close()
        print("Finished Relative Generation. painted {0} nodes".format(numEntities))

    def readMapFile(self, path):
        Config.new_map_data.clear()

        Config.loaded_new_map_flag = True
        highestID = 0
        data = None
        Node.id = 0
        Node.all().clear()
        with open(path, "r") as openFile:
            data = json.load(openFile)
        print("Read Map File ----------")
        pg.display.set_caption("Lance's World Builder ( Tool for CSCB58 Final Project ) READING: {0}".format(path))
        Config.new_map_data["ConflictingIDS"] = []
        from Generic.mapdata import MapData

        for index, props in enumerate(data):
            if props.__contains__("Name") and props["Name"] == MapData.Name:
                for k, v in props.items():
                    print("MAP DATA -> {0} = {1}".format(k, v))
                    setattr(MapData.get(), k, v)
                MapData.get().reload()
                resizeMap()
                continue
            
            nodeToLoad = Node(props["TopLeft"], props["BottomRight"], props["Color"])
            nodeToLoad.loadProperties(props)
            highestID = max(nodeToLoad.id, highestID)
            if props.__contains__("Name"):
                propName = props["Name"]
                if Config.new_map_data.__contains__(propName):
                    print("> Inserting to stored dict '{0}' size: {1}".format(propName, len(Config.new_map_data[propName])))
                    # Check if conflicting node id
                    if nodeToLoad.id in Config.new_map_data[propName][0]:
                        Config.new_map_data["ConflictingIDS"].append(nodeToLoad)
                    else:
                        Config.new_map_data[propName][0].append(nodeToLoad.id)
                        Config.new_map_data[propName][1][nodeToLoad.id] = nodeToLoad
                else:
                    print("+ Creating new key: {0}".format(propName))
                    Config.new_map_data[propName] = [[nodeToLoad.id], {nodeToLoad.id:nodeToLoad}]
            Node.addNode(nodeToLoad)
        print(">>>> Setting Node ID to {0}".format(highestID))
        Node.id = max(Node.id, highestID+1)
        print("Read Map File Finished ----")
        