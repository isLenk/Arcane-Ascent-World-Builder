import pygame as pg
from Abstracts.singleton import Singleton

class CursorHandler(Singleton):
    prevCursorIcon = pg.SYSTEM_CURSOR_ARROW
    currCursorIcon = pg.SYSTEM_CURSOR_ARROW

    prevCursorVisible = True
    currCursorVisible = True

    def setCursor(cursor):
        CursorHandler.currCursorIcon = cursor
    
    def setVisible(visible:bool):
        CursorHandler.currCursorVisible = visible

    def changedCursor(): return CursorHandler.prevCursorIcon != CursorHandler.currCursorIcon
    def changedVisibility(): return CursorHandler.prevCursorVisible != CursorHandler.currCursorVisible

    def update():
        if CursorHandler.changedCursor:
            pg.mouse.set_cursor(CursorHandler.currCursorIcon)
            CursorHandler.prevCursorIcon = CursorHandler.currCursorIcon
        if CursorHandler.changedVisibility:
            pg.mouse.set_visible(CursorHandler.currCursorVisible)
            CursorHandler.prevCursorIcon = CursorHandler.currCursorVisible
