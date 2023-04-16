import pygame as pg
# Events Interface
class Events:
    """Interface for classes that handle events"""
    def onMouseDown(self, *args): pass
    def onMouseUp(self, *args): pass
    def onMouseMotion(self, *args): pass
    def processEvent(self, event): pass

class Drawable:
    """Interface for classes needing update() and render()"""
    def update(self, *args): pass
    def render(self, *args): pass

class StaticDrawable:
    """Interface for static classes needing update() and render()"""
    def update(*args): pass
    def render(*args): pass

# Interface for Properties
class Properties:
    items = {}
    def __init__(self):
        self.items = {}
        for k, v in self.items.items():
            setattr(self, k, v)
    
    def addProperty(self, k, v):
        self.items[k] = v
        setattr(self, k, v)

    def getProps(self): return self.items

    def loadProperties(self, prop):
        for k, v in prop.items():
            self.addProperty(k, v)

class NodeProperties(Properties):
    def __init__(self):
        super().__init__()
        self.items['TopLeft'] = 0
        self.items['BottomRight'] = 0
        self.loadProperties(self.items)

class Page(StaticDrawable):
    name: str
    surface: pg.Surface

    def Preload(absTopLeft): pass
    
class FilesPage(Page, StaticDrawable): 
    name = "Files"
    def update(*args): pass
    def render(*args): pass
    
class Tool(Events, Drawable): 
    """YEAH"""
    def onToolSelect(self): pass
    def onToolDeselect(self): pass