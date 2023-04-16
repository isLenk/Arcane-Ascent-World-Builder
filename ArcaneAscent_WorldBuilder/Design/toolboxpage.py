from Interfaces import StaticDrawable, Page
import pygame as pg
from pygame import Color
from constants import *
from Design.toolboxitem import ToolboxItem
from Generic.helperfuncs import *
from Abstracts.singleton import Singleton

class ToolboxPage(Page, StaticDrawable):
    ListBackgroundColor = Color(45,49,68)
    HoverButtonColor = Color(66, 74, 102)
    InactiveButtonColor = Color(54, 60, 83)
    ActiveButtonColor = Color(22, 24, 33)
    ItemsPerRow = 3
    ButtonMargin = Vector2(5, 5)
    RectSize = PANEL_WIDTH/ItemsPerRow - ButtonMargin.x*2

    SelectedButton = None
    HoveredButton = None
    name = "Toolbox"

    def render(*args):
        ToolboxPage.HoveredButton = None
        absTopLeft = args[0]
        surface:pg.Surface = ToolboxPage.surface
        surface.fill(ToolboxPage.ListBackgroundColor)

        # Draw rect
        for i, v in enumerate(ToolboxItem.Collection):
            left = ToolboxPage.ButtonMargin.x + (i%ToolboxPage.ItemsPerRow)*(ToolboxPage.ButtonMargin.x + ToolboxPage.RectSize)
            top = ToolboxPage.ButtonMargin.y + (i//ToolboxPage.ItemsPerRow)*(ToolboxPage.ButtonMargin.y + ToolboxPage.RectSize)
            rect = pg.Rect(left, top, *([ToolboxPage.RectSize]*2))
            isHovering = rect.collidepoint(Vector2(Config.mousePos) - absTopLeft)
            if v == ToolboxPage.SelectedButton:
                pg.draw.rect(surface, ToolboxPage.ActiveButtonColor, rect, 0, 3)
            else:
                pg.draw.rect(surface, isHovering and ToolboxPage.HoverButtonColor or ToolboxPage.InactiveButtonColor, rect, 0, 3)
            
                if pg.mouse.get_pressed()[0] and isHovering:
                    ToolboxPage.SelectedButton = v
                    selectTool(v.get_tool())
            # ? Render icon
            surface.blit(v.get_icon(), (left, top))
