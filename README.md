# Arcane Ascent World Builder Tool
A python tool designed to draw on the Mars MIPS bitmap display.


<p align="middle">
    <img src="https://i.gyazo.com/4069494e3a8ceb1ce3bbe5bdfdd9919d.png" alt="An image of the program"/>
    <img src="https://i.gyazo.com/e0381dfd18130b92cbe84c60dcaf6f75.gif" alt="GIF of loading a file and generating the assembly code"/>
</p>

It is partially completed, lacks documentation, testing, optimization, and features. I may choose to update this to get a complete version. The complete version will be more useful to other people.

As of now, there are no designated buttons for a lot of the commands. Instead, the person must know the keyboard shortcuts to execute the commands. Additionally, internal status' are displayed in the console.

| <div style="width:80px">Key</div> | Purpose | Details |
| :---: | ------- | ------- |
| Tab | Change entity | Used in the entity tool, swaps between which entity is currently selected. |
| b | Open file dialog | Choose a map file to load. |
| c | Copy pixel color | Copies the color of the pixel that the mouse is over. |
| e | Delete node | Hover over a node and press 'e' to remove it
| f | Fill background | This function does not get converted to assembly. A tool to color the canvas background, useful for choosing the correct palette. |
| m   | Toggle generate by matching pixels | When enabled, Aligns same colored pixels and then draws by pixel, otherwise, uses fill function|
| o | Cycle layer generating type | Cycle between generating all layers, current layer, or current layer and layers below |
| q | Toggle restrict minimum flag | Allow the user to paint single tile walls. This is automatically disabled on brush tool |
| s | Generate map | Produces an `.asm` file containing the assembly code required to display the given map |
| SHIFT + s | Save map | If new canvas, produces a `workspace/maps/result.json` file that contains data required to load the map. If the map was loaded in, will save to the maps path. |
| ` | Toggle layering opacity | Layer transparency differs by distance from current layer. Enabling this will keep their opacity at full, and thus allow you to see it as if it were a flat image |
| 1-9 | Change current layer | Changes the current layer to whatever number was pressed. The layers are drawn in ascending order (i.e. layer 1 being bottommost and layer 9 being the top most) |



Created for my assembly game "Arcane Ascent": https://github.com/isLenk/ARCANE_ASCENT

### Dependencies
```python
pip install pygame
pip install pyauto_gui
pip install tk
```

Usage, `python ArcaneAscent_WorldBuilder/run.py`
# Features
- User friendly interface
    - It is oh-so-beautiful in my opinion
- Nine toolbox items
    1. Wall Tool
    2. Key Placer
    3. Exit Placer
    4. Enemy Spawn
    5. Player Spawn
    6. Spike Layer
    7. Pickup Placer
    8. Paintbrush
        - Comes with a cool color picker.
    9. Canvas Resize
        - Would not use. Really hard to use.
- Partially implemented features.
    - Again, this was written within a tight time schedule, the less important features have been ignored.
- Nine layered canvas.
    - Press 1-9 on the keyboard to cycle through them
- Saving / Loading
    - Drag and drop
    - File dialog (press b)
- Property viewer
    - Select a node to view its internal properties. (readonly for now)
- Node editor
    - Click a node to select it.
    - Drag node to move it
    - If the node has a `Resizable` property, drag the bottom right of node to resize.

For help in how to use this program, please hesitate to contact me on Discord @ `Lenk#9415`