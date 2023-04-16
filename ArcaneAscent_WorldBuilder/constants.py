from pygame import Vector2, Vector3
from enum import Enum
from pygame import Color
from pygame.locals import *
# PIXEL vs. FILL
# PIXEL is faster, accessing indexes
# FILL is shorter
DRAWING_METHOD = "FILL"

# ? Distance from the edge of the window.
PADDING = 10

# ? How much horizontal space is reserved on the left side of the 
# ? window for panels.
PANEL_WIDTH = 250
WINDOW_SIZE = Vector2(1240, 820)
CANVAS_SIZE = WINDOW_SIZE - (PADDING*3 + PANEL_WIDTH, 80)

TOOLBAR_WIDTH = 100

CANVAS_TOPLEFT = (WINDOW_SIZE[0]-CANVAS_SIZE[0]-PADDING, PADDING+25)
FPS = 30

# Define Colors 
WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

WINDOW_BG_COLOR = Color(41, 45, 62)
CANVAS_COLOR = Color(32, 35, 49)
CANVAS_DOTS = Color(22, 25, 39)
MOUSE_OVER_NODE_COLOR = Color(130, 170, 255)
NODE_EDIT_COLOR = Color(103, 132, 219)
NODE_EDIT_RESIZE_COLOR = Color(103, 132, 219, 200)
SEMI_OPAQUE = Color(250,120,110, 100)
EMPTY_COLOR = Color(0,0,0,0)
CREDIT_COLOR = Color(22, 24, 23)

PLATFORM_COLOR = Color("#5c5454") # BLACK

TwoPanelFrontTextColor = Color(222,222,222)
TwoPanelBackTextColor = Color(72,79,108)
PanelBackgroundColor = Color(54,60,83)
PanelSecondaryColor = Color(32,35,49)
# .eqv	COLOUR_BG			0x00171616 # 0x00000001 		# Original Blue - 0x0026305e
# .eqv	WALL_COLOR			0x005c5454 	# 0x00171717 		# Light Gray
FILE_EXTENSION = ".json"
GAME_SCREEN_DIMENSIONS = (4, 512, 384)
FULL_SCREEN_DIMENSIONS = (4, 512, 512)
DEFAULT_DIMENSIONS = GAME_SCREEN_DIMENSIONS # FULL_SCREEN_DIMENSIONS # 

# Layers opacity = 255 - LAYERING_OPACITY_CHANGE_BY_DISTANCE*(distance from current layer)
LAYERING_OPACITY_CHANGE_BY_DISTANCE = 30

KEYBINDS = {
    "toggle_matching_pixels_generated": K_m,
    "toggle_restrict_min_flag": K_q,
    "generate_map_flag": K_s,
    "SAVE_MAP": K_s,
    "LOAD_MAP_FILE": K_b,
    "FILL_BACKGROUND": K_f,
    "COPY_MOUSEPIXEL": K_c,
    "TOGGLE_LAYERING_OPACITY": K_BACKQUOTE,
    "CHANGE_CANVAS_LAYER1": K_1,
    "CHANGE_CANVAS_LAYER2": K_2,
    "CHANGE_CANVAS_LAYER3": K_3,
    "CHANGE_CANVAS_LAYER4": K_4,
    "CHANGE_CANVAS_LAYER5": K_5,
    "CHANGE_CANVAS_LAYER6": K_6,
    "CHANGE_CANVAS_LAYER7": K_7,
    "CHANGE_CANVAS_LAYER8": K_8,
    "CHANGE_CANVAS_LAYER9": K_9,
    "layer_generating_type": K_o,
    "CHANGE_ENTITY": K_TAB
}

class Entity:
    Name: str
    Color: list
    Size: set
    id: int

    def __init__(self, id, Name, Color, Size):
        self.id = id
        self.Name = Name
        self.Color = list(Color)
        self.Size = list(Size)

ENTITY_DATA_SIZE = 8
ENTITY_ARRAY_LIMIT = 15

class EntityCycler:
    _ENTITIES = [
        Entity(4, "HEALTH_RESTORE", Color(255, 65, 51), (3,3)),
        Entity(5, "GRAVITY_POTION", Color(255, 255, 255), (3,4)),
        Entity(6, "FLIGHT_POTION", Color(103, 193, 245), (3, 4)),
        Entity(7, "DRUNK_POTION", Color(158, 97, 84), (3, 4)),
        Entity(8, "SPELL_RECHARGE", Color(176, 115, 255), (3, 3))
    ]

    ChosenEntity = -1

    def get(name):
        """Return the entity object with the name 'name' """
        for v in EntityCycler._ENTITIES:
            if v.Name == name: return v
        return None
    
    def getNext():
        EntityCycler.ChosenEntity = (EntityCycler.ChosenEntity+1)%len(EntityCycler._ENTITIES)
        return EntityCycler._ENTITIES[EntityCycler.ChosenEntity]

# Used in coin tool. Coin tool is a very misleading name, in actuallity, the tool is an pickup tool.
# It allows you to set different pickup item positions.

# nodes = []

def addColor(color, add):
    if type(add) == type(0):
        add = (add, add, add)
    alpha = 255
    if len(color) > 3:
        alpha = color[3]
    color = color[:3]
    try:    # i am not going to fix this
        newCol = Vector3(color) + add
        return (max(0, min(255,newCol.x)), max(0, min(255,newCol.y)), max(0, min(255,newCol.z)), alpha)
    except:
        return color