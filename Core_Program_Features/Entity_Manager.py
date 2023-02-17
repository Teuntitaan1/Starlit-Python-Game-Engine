import Core_Program_Features


class EntityManager:
    def __init__(self):
        self.EntityList = []

    def update(self, windowmanager: Core_Program_Features.Window, gameinfo: Core_Program_Features.GameInfo):
        for entity in self.EntityList:
            entity.update(gameinfo)
            windowmanager.render(entity.return_render_data())

    def add_entity(self, entity):
        self.EntityList.append(entity)

    def remove_entity(self, entity):
        self.EntityList.remove(self.EntityList.index(entity))
