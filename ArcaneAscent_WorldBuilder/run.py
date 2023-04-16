# Developed to use in my MIPS Assembly Game Project
# OS : Written on Windows 11
# * Dimensions
# * 512x512
# * 4x4 unit size
# * Base Address 0x10008000 ($gp)

import pygame as pg

pg.init()
pg.font.init()

import Generic.config as Config
from Generic.helperfuncs import *
import os
import sys
from pygame.locals import *
from constants import *
from pathlib import Path

mapData = MapData.instance(*DEFAULT_DIMENSIONS)

# Color picker
import pygame_gui

# File loading
from tkinter.filedialog import askopenfilename 
from tkinter import *

from Interfaces import *
from Generic import *

from Generic.cursorhandler import CursorHandler
from filemanager import FileManager
from Generic.objecthandler import ObjectHandler
from Generic.node import Node
from Generic.nodeeditor import NodeEditor
from Design.toolboxpage import ToolboxPage
from Design.canvas import Canvas
import Tools

Config.screen               = pg.display.set_mode(WINDOW_SIZE)
Config.above_screen         = pg.Surface(Config.screen.get_size(), pg.SRCALPHA)
Config.canvas               = pg.Surface(CANVAS_SIZE)
Config.map_canvas_overlay   = pg.Surface(mapData.getMapSize(), pg.SRCALPHA)
Config.overlay              = pg.Surface(WINDOW_SIZE, pg.SRCALPHA)
Config.indicator_overlay    = pg.Surface(CANVAS_SIZE, pg.SRCALPHA)

# map_base_canvas is filled with BGColor, you cannot draw on this layer.
Config.map_base_canvas = pg.Surface(mapData.getMapSize(), pg.SRCALPHA)
Config.map_layers = [
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA),
    pg.Surface(mapData.getMapSize(), pg.SRCALPHA)
]


Config.map_canvas = None
Config.map_canvas_overlay.set_alpha(60)

Config.directory_path = os.path.join("../", os.path.dirname(Path(__file__).parent))
Config.ui_manager = pygame_gui.UIManager(
    Config.screen.get_size(), 
    os.path.join(os.path.dirname(Path(__file__)), "pygame_gui_theme.json"))
Config.ui_manager.live_theme_updates = False

pg.display.set_caption("Lance's World Builder ( Tool for CSCB58 Final Project )")
clock = pg.time.Clock()


FileManager.instance()

Config.currentNodeID = 0

Config.new_map_data = dict()

def checkArgs():
    if len(sys.argv) == 1: return
    loadFile(sys.argv[1])

# Check if player has passed a file containing a map
checkArgs()

onMouseDownPos = None
Config.mousePos = (0, 0)
Config.onMD_cell = None

infoFont = pg.font.SysFont('Helvetica', 15)
smallerInfoFont = pg.font.SysFont('Helvetica', 13)

# ? Objects added to this collection will have their logic done after 
# every unique instance has been completed


Config.colour_picker = None                                    
Config.current_colour = pg.Color(0, 0, 0)
Config.picked_colour_surface = pg.Surface((30, 30))
Config.picked_colour_surface.fill(Config.current_colour)

# Initialize Objects
NodeEditor.instance()
focusOnLayer(0)
Canvas.instance(Config.canvas)
running = True



Config.ToolSelected = None
Config.can_change_tool = True


starting_tool = Tools.init()
selectTool(starting_tool.get_tool())
# ? Sets default
ToolboxPage.SelectedButton = starting_tool
# ****************************

# Render static texts
creditText = "CSCB58 Assembly Game Map Builder | Written by Lance Talban"
credit = smallerInfoFont.render(creditText, True, CREDIT_COLOR)

def handleConflictingIDs(conflictingIds):
    ids = []
    if len(conflictingIds) == 0: print(">> No conflicting IDs gathered.") 
    
    # Parse all conflicting ids
    for node in Node.all():
        if not ids.__contains__(node.id):
            ids.append(node.id)

    # Get id's that are not used
    freeIDs = [x for x in range(Node.id+len(conflictingIds)) if x not in ids]
    freeIDs = set(freeIDs) # Convert to a set to pop.

    changes = 0
    for node in conflictingIds:
        for tool in Config.placing_tool_collection:
            if tool.CustomAttributes.__contains__("Name"):
                toolName = tool.CustomAttributes["Name"]
                if toolName != node.Name: continue

                # Determine if the current node is not the conflicting id
                # This shouldn't happen.
                if node.id not in tool.children: continue
                if tool.NOT_SAVED["children"][node.id] == node: continue

                oldID = node.id
                # Assign a new id
                newId = freeIDs.pop()

                node.id = newId
                # node.Color = CONFLICT_ID_COLOR
                # TODO: Implement a method for this b/c its repeated in tool
                tool.children.append(node.id)
                tool.NOT_SAVED["children"][node.id] = node

                # Update nodes current ID if lower
                if newId > Node.id: Node.id = newId + 1

                print("| {0} Node ID Changed ({1} -> {2})".format(toolName, oldID, node.id))
                changes += 1

    print(">> Resolved {0} conflicts.".format(changes))

def askFileToLoad():
    root = Tk()
    success = askopenfilename(title="Select map to load...", filetypes=[("Map Type", "*{0}".format(FILE_EXTENSION))], initialdir=FileManager.get().mapsFolder)
    root.destroy()
    if success == "": return
    loadFile(success)
    
# ? Lazy fix to incorrect size generation 
Config.generate_map_flag = 0
Config.restrict_min_flag = True # Prevents 1x1 nodes
Config.matching_pixels_generated = False

def main():
    running = True
    while running:

        Config.keySelected = []
        time_delta = clock.tick(FPS) / 1000
        events = pg.event.get()
        Config.stepHasLeftClick = False    # Cheeky fix for preventing event bugs

        for event in events:
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEMOTION:
                shift_amount = pg.mouse.get_rel()
                Config.mousePos = pg.mouse.get_pos()

                Config.ToolSelected.onMouseMotion(event)
                Canvas.get().onMouseMotion(shift_amount)
                NodeEditor.get().onMouseMotion(event)
                
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button ==  pg.BUTTON_RIGHT:
                    NodeEditor.get().isResizing = False
                if event.button ==  pg.BUTTON_LEFT:
                    Config.stepHasLeftClick = True
                    if mapFocused(Config.mousePos):
                        Config.onMD_cell = getCell(Config.mousePos)

                NodeEditor.get().onMouseDown(event)
                if not NodeEditor.get().isOverResizeButton:
                    Config.ToolSelected.onMouseDown(event)
                    if event.button == 3 and Canvas.get().isDragging == False:
                        Canvas.get().isDragging = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == pg.BUTTON_LEFT:
                    if NodeEditor.get().isResizing: 
                        NodeEditor.get().isResizing = False
                        NodeEditor.get().setTarget(None)

                    if NodeEditor.get().isMouseDown: NodeEditor.get().isMouseDown = False

                    if NodeEditor.get().HoveringOn:
                        NodeEditor.get().setTarget(NodeEditor.get().HoveringOn)
                    else:
                        if NodeEditor.get().Target:
                            # If editing node and select outside of node, deselect node to edit
                            NodeEditor.get().TargetRect = computeAreaAsRect(NodeEditor.get().Target.TopLeft, NodeEditor.get().Target.BottomRight)
                            if not NodeEditor.get().TargetRect.collidepoint( posRelativeToMap(Config.mousePos)):
                                NodeEditor.get().setTarget(None)
                    Config.ToolSelected.onMouseUp(event)


                elif event.button == 3:
                    Canvas.get().isDragging = False
                
            elif event.type == MOUSEWHEEL:

                if canvasFocused(Config.mousePos):
                    if (event.y > 0):
                        Config.scale += 0.1
                    elif (event.y < 0):
                        Config.scale = max(0.1, Config.scale - 0.1)
                    resizeMap()
                        
            elif event.type == pg.KEYUP:
                mods = pg.key.get_mods()
                Config.keySelected.append(event.key)
                if mods & pg.KMOD_LSHIFT and event.key == KEYBINDS["SAVE_MAP"]:
                    print(">> Saving Map...")
                    FileManager.get().saveMapFile("results", Node.all())
                elif event.key == KEYBINDS["generate_map_flag"]:
                    Config.scale = 1
                    Config.generate_map_flag = 1
                elif event.key == KEYBINDS["toggle_restrict_min_flag"]:
                    Config.restrict_min_flag = not Config.restrict_min_flag
                    print(">> Restrict Min = {0}".format("Enabled" if Config.restrict_min_flag else "Disabled"))
                elif event.key == KEYBINDS["toggle_matching_pixels_generated"]:
                    Config.matching_pixels_generated = not Config.matching_pixels_generated
                    print(">> {0} Matching Generated Style".format("Enabled" if Config.matching_pixels_generated else "Disabled"))
                elif event.key == KEYBINDS["LOAD_MAP_FILE"]:
                    askFileToLoad()
                elif event.key == KEYBINDS["TOGGLE_LAYERING_OPACITY"]:
                    Config.layering_opacity_enabled = not Config.layering_opacity_enabled
                    setLayerOpacities(Config.current_canvas_layer)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER1"]: focusOnLayer(0)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER2"]: focusOnLayer(1)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER3"]: focusOnLayer(2)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER4"]: focusOnLayer(3)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER5"]: focusOnLayer(4)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER6"]: focusOnLayer(5)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER7"]: focusOnLayer(6)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER8"]: focusOnLayer(7)
                elif event.key == KEYBINDS["CHANGE_CANVAS_LAYER9"]: focusOnLayer(8)
                elif event.key == KEYBINDS["layer_generating_type"]: 
                    Config.layer_generating_type = (Config.layer_generating_type+1)%3
            elif event.type == pg.DROPFILE:
                loadFile(event.file)
                
            Config.ToolSelected.processEvent(event)
            Config.ui_manager.process_events(event)
            ObjectHandler.processEvent(event)

        Config.ui_manager.update(time_delta)
        # *******************************************************************
        # * GAME LOGIC

        if Config.generate_map_flag == 2:
            Config.generate_map_flag = 0
            print(">> Generating Map...")
            FileManager.get().generate(Node.all())
            resizeMap()
            Config.map_origin = CANVAS_SIZE/2 - (mapData.getMapSize())/2
        if Config.generate_map_flag == 1: Config.generate_map_flag = 2

        Config.ToolSelected.update()
        NodeEditor.get().update()
        ObjectHandler.update()
        # ? Update Cursor
        CursorHandler.update()
        
        # *******************************************************************
        # * GAME DRAW

        #3 Draw/render
        Config.screen.fill(WINDOW_BG_COLOR)
        Config.canvas.fill(CANVAS_COLOR)
        
        Config.map_base_canvas.fill(Config.map_bg_color)
        # Iterate through Config.canvas'
        for canvasLayer in Config.map_layers: canvasLayer.fill(EMPTY_COLOR)

        Config.overlay.fill(EMPTY_COLOR)
        Config.map_canvas_overlay.fill(EMPTY_COLOR)
        Config.above_screen.fill(EMPTY_COLOR)

        NodeEditor.get().HoveringOn = None
        NodeEditor.get().isOverResizeButton = False

        for node in Node.all():
            rect = computeAreaAsRect(node.TopLeft, node.BottomRight)
            # Check if colliding
            isHovering = rect.collidepoint( posRelativeToMap(Config.mousePos) )
            onCurrentLayer = node.Layer == Config.current_canvas_layer
            # Let NodeEditor.get() handle drawing its target
            if node is NodeEditor.get().Target:
                # nodeColor = NODE_EDIT_COLOR
                NodeEditor.get().render(Config.map_canvas, node.Color, rect)
            else:
                nodeColor = (onCurrentLayer and isHovering) and addColor(node.Color, (20, 20, 40)) or node.Color
                pg.draw.rect(Config.map_layers[node.Layer], nodeColor, rect)
            # Delete instance.     
            if (K_e in Config.keySelected and isHovering and onCurrentLayer):
                node.delete()
                if node is NodeEditor.get().Target: 
                    NodeEditor.get().setTarget(None)
            if isHovering and onCurrentLayer:
                NodeEditor.get().HoveringOn = node

        Config.ToolSelected.render()
        ObjectHandler.render()

        generatingTypeText = "Draw All Layers"
        if Config.layer_generating_type == 1:  generatingTypeText = "Draw Current Layer"
        elif Config.layer_generating_type == 2: generatingTypeText = "Draw Current Layer and All Below"
        currentLayer = infoFont.render(str("LAYER {0} | {1}".format(Config.current_canvas_layer+1, generatingTypeText)), True, WHITE)

        Canvas.get().render()
        Config.screen.blit(currentLayer, CANVAS_TOPLEFT - Vector2(0, 20))
        Config.screen.blit(Config.canvas, CANVAS_TOPLEFT)
        Config.screen.blit(Config.overlay, (0,0))
        Config.screen.blit(credit, WINDOW_SIZE - smallerInfoFont.size(creditText) - (10, 10))
        Config.screen.blit(Config.above_screen, (0,0))
        ## Done after drawing everything to the Config.screen
        pg.display.flip()  

        # Check for new map loaded (side note, if is not needed)
        if Config.loaded_new_map_flag: 
            for tool in Config.placing_tool_collection:
                if tool.CustomAttributes.__contains__("Name"):
                    toolName = tool.CustomAttributes["Name"]
                    # Check if the new map contains this entity
                    if not Config.new_map_data.__contains__(toolName): 
                        print("Entity type(\"{0}\") not in map.".format(toolName))
                        continue

                    tool.children.clear()
                    tool.children = Config.new_map_data[toolName][0]
                    tool.NOT_SAVED["children"] = Config.new_map_data[toolName][1]
                    print(tool.CustomAttributes["Name"], tool.children)

                    # Load all the NOT_SAVED data

                    # ? Lazy fix: Disables canPlace if reached entity limit
                    print(toolName, tool.EntityLimit, len(tool.children))
                    tool.canPlace = (tool.EntityLimit > len(tool.children))
                handleConflictingIDs(Config.new_map_data["ConflictingIDS"])
            Config.new_map_data.clear()
            Config.loaded_new_map_flag = False

    pg.quit()




if __name__ == "__main__":
    main()

