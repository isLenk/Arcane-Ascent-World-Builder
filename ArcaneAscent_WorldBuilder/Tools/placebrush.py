from Tools.drag import DragTool
import Generic.config as Config
from Generic.helperfuncs import *
from constants import *
from filemanager import FileManager
import pygame as pg
from Generic.nodeeditor import NodeEditor
from pygame_gui.windows import UIColourPickerDialog
import pyautogui
import pygame_gui
from pygame_gui.elements import UIButton
from Generic.node import Node

fileManager: FileManager

infoFont = pg.font.SysFont('Helvetica', 15)
class PlaceBrushTool(DragTool):
    # hitboxSize = (4,2)
    # hitboxColor = Color(100, 100, 100)
    EntityLimit = 999
    CustomAttributes = {
        "Name": "BrushPixel",
        "Color": (0, 0, 0),
        "Resizable" : True
    }

    def __init__(self, *args):
        global fileManager
        super().__init__(*args)
        fileManager = FileManager.instance()

        Config.colour_picker_button = UIButton(
            relative_rect=pg.Rect( (CANVAS_TOPLEFT + Vector2(40, 10)), (150, 30)),
            text = "Pick Colour",
            manager = Config.ui_manager)

    RestrictMinOnLoad = None
    def changeBrushColor(self, color):
        Config.current_colour = Color(color)
        Config.picked_colour_surface.fill(Config.current_colour)
        self.CustomAttributes["Color"] = list(Config.current_colour)

    def drawByFill(self):
        print(">> GENERATING BY FILL")
        content = ""
        
        # Organize the nodes by their colour
        sorted_nodes = {}
        childIDs, childNodes = self.get_children()
        for id in childIDs:
            child = childNodes[id]
            nodeColour = mipsRGBtoHex(*child.Color[:3])
            if sorted_nodes.__contains__(nodeColour):
                sorted_nodes[nodeColour].append(child)
            else:
                sorted_nodes[nodeColour] = [child]

        for current_layer in range(len(Config.map_layers)):

            if Config.layer_generating_type == 1 and current_layer != Config.current_canvas_layer: continue
            if Config.layer_generating_type == 2 and current_layer > Config.current_canvas_layer: continue
            content += "# Drawing Layer {0}\n".format(current_layer+1)
            for colour, nodes in sorted_nodes.items():
                # Check there exists atleast one child in this layer.
                hasNode = False
                for child in nodes: 
                    if child.Layer == current_layer:
                        hasNode = True
                        break
                if not hasNode: continue # This layer has no kids

                content += "li $a3, {0}\n".format(colour)
                for child in nodes:
                    if child.Layer != current_layer: continue # Node belongs to different layer
                    node = computeAreaAsRect(child.TopLeft, child.BottomRight)
                    startPos = getAssemblyPos(node.topleft)
                    content += "lw $t0, 0($sp)\n"
                    content += "addi $t0, $t0, {0}\n".format(int(startPos))
                    #nodeHeight = node.height//mapData.unitSize
                    #nodeWidth = node.width//mapData.unitSize
                    nodeHeight = child.BottomRight[1] - child.TopLeft[1]
                    nodeWidth = child.BottomRight[0] - child.TopLeft[0] + 1
                    nodeEndPos = (nodeHeight)*((MapData.get().copyDisplayWidth//MapData.get().copyUnitSize)*4) + nodeWidth*4

                    # Store the start position
                    content += "move $a0, $t0\n"
                    # Shift $t0 to the end position
                    content += "addi $t0, $t0, {0}\n".format(int(nodeEndPos))
                    content += "move $a1, $t0\n"
                    # Set row length to the width
                    content += "li $a2, {0}\n".format(int(nodeWidth*4-4))
                    content += "jal FILL\n"
                content += "\n"
        return content
    
    def drawByPixel(self):
        print(">> GENERATING BY PIXEL")
        # node: Rect = computeAreaAsRect(nodeData.TopLeft, nodeData.BottomRight)
        content = ""
        
        # Organize the nodes by their colour
        sorted_nodes = {}
        childIDs, childNodes = self.get_children()
        for id in childIDs:
            child = childNodes[id]
            nodeColour = mipsRGBtoHex(*child.Color[:3])
            if sorted_nodes.__contains__(nodeColour):
                sorted_nodes[nodeColour].append(child)
            else:
                sorted_nodes[nodeColour] = [child]

        # Now print
        
        for current_layer in range(len(map_layers)):
            if Config.layer_generating_type == 1 and current_layer != Config.current_canvas_layer: continue
            if Config.layer_generating_type == 2 and current_layer > Config.current_canvas_layer: continue
            for colour, nodes in sorted_nodes.items():
                # content += "# Drawing Layer {0}\n".format(current_layer+1)
                # Check there exists atleast one child in this layer.
                hasNode = False
                for child in nodes: 
                    if child.Layer == current_layer:
                        hasNode = True
                        break
                if not hasNode: continue # This layer has no kids

                content += "li $t0, {0}\n".format(colour)
                for index, node in enumerate(nodes):
                    numCellsX = (node.BottomRight[0] - node.TopLeft[0]) + 1
                    numCellsY = (node.BottomRight[1] - node.TopLeft[1]) + 1
                    # print("Node ({0})".format(node.id), numCellsX, numCellsY)
                    
                    for x in range(int(numCellsX)):
                        for y in range(int(numCellsY)):
                            #nodeRect: Rect = computeOriginalAreaAsRect( node.TopLeft + Vector2(x,y), node.BottomRight)
                            # position = getAssemblyPosUsingIndex(nodeRect.topleft)
                            position = getAssemblyPosBINDEX(node.TopLeft[0] + x, node.TopLeft[1] + y)
                            content += "sw $t0, {0}($a0)\n".format(int(position))
                    
                content += "\n\n"
            #content += "addi	$sp, $sp, 4\n"
        return content
    
    def generate(self):
        # Ignore if there are no items to generate.
        if len(self.children) == 0: return;
        content = "\n\nBRUSH_TOOL_RESULT:\n"
        content += FileManager.pushRA()
        content += "addi $sp, $sp, -4\nsw $a0, 0($sp)\n"
        content += self.drawByPixel() if Config.matching_pixels_generated else self.drawByFill()        
        content += "addi	$sp, $sp, 4\n"
        content += FileManager.popRA()
        content = content.replace("\n", "\n\t")
        return content

    def onToolSelect(self): 
        self.RestrictMinOnLoad = Config.restrict_min_flag
        Config.restrict_min_flag = False

    def onToolDeselect(self):
        Config.restrict_min_flag = self.RestrictMinOnLoad
        focusOnLayer(0)

    def onMouseMotion(self, *args):
        if self.isDragging: return
        self.isDragging = self.isDragging == None and mapFocused(Config.mousePos)

    def onMouseUp(self, *args):
        if (self.isDragging or self.isDragging==None):
            self.awaitingDraw = True and mapFocused(Config.mousePos)
            self.isDragging = False

    def onMouseDown(self, *args):
        if Config.can_change_tool == False or NodeEditor.get().Target is not None: return
        event = args[0]
        if event.button !=  pg.BUTTON_LEFT: return
        if not mapFocused(Config.mousePos) or not self.rect: return
        if not self.canPlace: return
        self.isDragging = None
    
    def processEvent(self, event):
       
        if event.type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == Config.colour_picker_button:
            Config.can_change_tool = False
            Config.colour_picker = UIColourPickerDialog(
                pg.Rect(150, 50, 400, 400), 
                Config.ui_manager,
                window_title="Change Brush Color...", 
                initial_colour=Config.current_colour)

        if event.type == pygame_gui.UI_COLOUR_PICKER_COLOUR_PICKED:
            self.changeBrushColor(event.colour)
        if event.type == pygame_gui.UI_WINDOW_CLOSE:    
            Config.can_change_tool = True
        if event.type == pg.KEYUP:
            if event.key == KEYBINDS["FILL_BACKGROUND"]:
                Config.map_bg_color = list(Config.current_colour)
            elif event.key == KEYBINDS["COPY_MOUSEPIXEL"]:
                # Check if hovering over a node
                if mapFocused(Config.mousePos):
                    if NodeEditor.get().HoveringOn:   # Copy color of hovered pixel
                        self.changeBrushColor(NodeEditor.get().HoveringOn.Color)
                    else:   # Copy background color
                        self.changeBrushColor(Config.map_bg_color)
                else:   # Hover pixel on Config.screen
                    x, y = pyautogui.position()
                    px = pyautogui.pixel(x, y)
                    self.changeBrushColor(px)
                
    def render(self, *args): 
        Config.above_screen.blit(Config.picked_colour_surface, CANVAS_TOPLEFT + Vector2(10, 10))
        Config.ui_manager.draw_ui(Config.above_screen)

        if Config.can_change_tool == False: return
        self.canPlace = (self.EntityLimit > len(self.children))
        # ? Hide cursor when over map.
        # CursorHandler.setVisible(not mapFocused(mousePos))
        
        # ? Show Drag Box
        if mapFocused(Config.mousePos) and self.isDragging and not NodeEditor.get().Target and Config.onMD_cell is not None:
            endPos = getCell(Config.mousePos)
            startRect = computeAreaAsRect(Config.onMD_cell, endPos)
            pg.draw.rect(Config.map_canvas, Config.current_colour, startRect)

        # ? Show indicators
        if (mapFocused(Config.mousePos)):
            currentCell = infoFont.render(str(getCell(Config.mousePos)), True, BLACK)
            Config.overlay.blit(currentCell, Vector2(Config.mousePos)+(15, 15)) 
            rect = getNode(Config.mousePos)

            yRect = rect.copy()
            xRect = rect.copy()

            xRect.left = 0
            xRect.width = Config.map_canvas.get_width()

            yRect.top = 0
            yRect.height = Config.map_canvas.get_height()

            pg.draw.rect(Config.map_canvas_overlay, Color(150,150,150), yRect)
            pg.draw.rect(Config.map_canvas_overlay, Color(150,150,150), xRect)
            pg.draw.rect(Config.map_canvas, MOUSE_OVER_NODE_COLOR, rect)

    def update(self, *args):
        global onMD_cell
        # ------------------------------------------------------------------
        if (self.awaitingDraw and NodeEditor.get().HoveringOn is not None): self.awaitingDraw = False
        # ------------------------------------------------------------------
        
        # ? Create the new node.
        if (mapFocused(Config.mousePos) and self.awaitingDraw and Config.onMD_cell is not None):
            self.awaitingDraw = False

            endPos = getCell(Config.mousePos)
            # * Add to node list.
            S, E = fixOrder(Config.onMD_cell, endPos)
            
            nodeSize = E-S
            if Config.restrict_min_flag == False or (nodeSize.x > 0 or nodeSize.y > 0):   # Build if larger than a pixel
                onMD_cell = None
                child = Node(S, E, list(self.CustomAttributes["Color"]))
                Node.addNode(child, self.children)
                self.children.append(child.id)
                self.NOT_SAVED["children"][child.id] = child
                self.applyAttributes(child)
