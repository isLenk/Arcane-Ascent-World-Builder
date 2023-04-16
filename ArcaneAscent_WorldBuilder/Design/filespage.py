from Interfaces import Page, StaticDrawable
from Abstracts.singleton import Singleton

class FilesPage(Singleton, Page, StaticDrawable): 
    name = "Files"
    def update(*args): pass
    def render(*args): pass
