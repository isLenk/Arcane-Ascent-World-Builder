from Interfaces import Drawable
from Abstracts.singleton import Singleton

class ObjectHandler(Singleton):
    Collection = list()
    EventListenerCollection = list()
    def add(instance: Drawable, isUpdatable=True): 
        ObjectHandler.Collection.append([instance, isUpdatable])

    def addEventListener(instance):
        ObjectHandler.EventListenerCollection.append(instance)
    
    def render(): 
        for v, _ in ObjectHandler.Collection: v.render()
    def update():
        for v, canUpdate in ObjectHandler.Collection: 
            if canUpdate: v.update()

    def processEvent(event):
        for v in ObjectHandler.EventListenerCollection:
            v.processEvent(event)
