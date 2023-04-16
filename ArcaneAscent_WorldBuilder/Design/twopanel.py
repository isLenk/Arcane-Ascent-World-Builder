import pygame as pg
from Design.panel import Panel
from pygame import Color, Vector2
from constants import *
from Interfaces import Page
import Generic.config as Config

tabFont = pg.font.SysFont("Century Gothic", 13)
class TwoPanel(Panel):
    TabHeight = 30
    HoverButtonColor = Color(23, 26, 36)
    TabPadding = (20, 5)
    inactiveSizeOffset = (3, 3)
    PagePadding = Vector2(5, 5)
    leftSelected = True
    HeightOnLeftSide = -1
    
    def __init__(self, left: Page, right: Page):
        self.left = left
        self.right = right

        self.leftActiveLabel = tabFont.render(left.name, True, TwoPanelFrontTextColor)
        self.rightActiveLabel = tabFont.render(right.name, True, TwoPanelFrontTextColor)
        self.leftInactiveLabel = tabFont.render(left.name, True, TwoPanelBackTextColor)
        self.rightInactiveLabel = tabFont.render(right.name, True, TwoPanelBackTextColor)

        rect = pg.Rect(PADDING, PADDING, PANEL_WIDTH, 150)
        super().__init__(rect)

    def setLeftSideHeight(self, height): 
        self.HeightOnLeftSide = height

    def generatePageSurfaces(self):
        lSurfSize = Vector2(self._rect.size) - (0,self.TabHeight) - self.PagePadding*2
        if self.HeightOnLeftSide > 0:
            lSurfSize = Vector2(self._rect.width, self.HeightOnLeftSide) - (0,self.TabHeight) - self.PagePadding*2
        lSurface = pg.Surface(lSurfSize, pg.SRCALPHA)
        rSurface = pg.Surface(Vector2(self._rect.size) - (0,self.TabHeight) - self.PagePadding*2, pg.SRCALPHA)
        self.left.surface  = lSurface 
        self.right.surface = rSurface

        absTopLeft = Vector2(self._rect.topleft) + (0, self.TabHeight) + self.PagePadding

        self.left.Preload(absTopLeft)
        self.right.Preload(absTopLeft)
    
    def update(self, *args):
        if self.leftSelected:
            self.left.update(*args)
        else:
            self.right.update(*args)

    def render(self, *args):
        
        copyRect = self._rect.copy()
        if self.leftSelected and self.HeightOnLeftSide > 0:
            copyRect.height = self.HeightOnLeftSide
            copyRect.bottom = self._rect.bottom
        # * Draw tab + body
        leftTabRect = copyRect.copy()
        rightTabRect = copyRect.copy()
        bodyRect = copyRect.copy()

        leftTabRect.height = self.TabHeight
        leftTabRect.width = tabFont.size(self.left.name)[0] + self.TabPadding[0]*2

        rightTabRect.height = self.TabHeight
        rightTabRect.width = tabFont.size(self.right.name)[0] + self.TabPadding[0] * 2

        if self.leftSelected:
            rightTabRect.right -= self.inactiveSizeOffset[0]
            rightTabRect.top += self.inactiveSizeOffset[1]

        else:
            leftTabRect.left += self.inactiveSizeOffset[0]
            leftTabRect.top += self.inactiveSizeOffset[1]
            rightTabRect.width = bodyRect.width - leftTabRect.width - self.inactiveSizeOffset[0]

        rightTabRect.left = leftTabRect.right
        bodyRect.top += self.TabHeight
        bodyRect.height -= self.TabHeight

        isHoveringLeft = leftTabRect.collidepoint(Vector2(Config.mousePos))
        isHoveringRight = rightTabRect.collidepoint(Vector2(Config.mousePos))
        mouseLeftDown = pg.mouse.get_pressed()[0]

        # * Handle Hover Check
        if self.leftSelected:                
            if isHoveringRight and mouseLeftDown: self.leftSelected = False
        else:
            if isHoveringLeft and mouseLeftDown: self.leftSelected = True

        # * Draw labels on the tabs
        leftTabPos =  Vector2(leftTabRect.topleft) + self.TabPadding
        rightTabPos =  Vector2(rightTabRect.topleft) + self.TabPadding

        inactiveIsHovered = ((not self.leftSelected and isHoveringLeft) or 
                            (self.leftSelected and isHoveringRight)) and \
                            self.HoverButtonColor or PanelSecondaryColor 
        pg.draw.rect(Config.screen, PanelBackgroundColor, self.leftSelected and leftTabRect or rightTabRect)
        pg.draw.rect(Config.screen, inactiveIsHovered, self.leftSelected and rightTabRect or leftTabRect)
        pg.draw.rect(Config.screen, PanelBackgroundColor, bodyRect)
        Config.screen.blit(self.leftSelected and self.leftActiveLabel or self.leftInactiveLabel, leftTabPos)
        Config.screen.blit(self.leftSelected and self.rightInactiveLabel or self.rightActiveLabel, rightTabPos)

        if self.leftSelected:
            self.left.render(bodyRect.topleft + self.PagePadding)
            Config.screen.blit(self.left.surface, bodyRect.topleft + self.PagePadding)
        else:
            self.right.render(bodyRect.topleft + self.PagePadding)
            Config.screen.blit(self.right.surface, bodyRect.topleft + self.PagePadding)
