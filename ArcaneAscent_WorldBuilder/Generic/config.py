from pygame import Color

map_origin = (0, 0)
map_canvas = None
# 0 = All
# 1 = Current Layer
# 2 = Current Layer + layers below
layer_generating_type = 0
layering_opacity_enabled = True
placing_tool_collection = list()
current_canvas_layer = -1
directory_path = ""
loaded_new_map_flag = False
scale = 1
map_bg_color = Color("#171616")#Color(194, 196, 207) #Color(54,14,25)