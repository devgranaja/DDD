
# ======================================================================================================================
# Entities
#

class Entity(object):
    """The base class of all entities.

    Attributes:
        id: A unique identifier.
    """

    def __init__(self, id):
        self._id = id

    def __eq__(self, ent):
        return self._id == ent.id

    @property
    def id(self):
        """A string unique identifier for the entity."""
        return self._id


# ======================================================================================================================
# Factories
#
class EntityFactory:
    factories = {}

    @staticmethod
    def addFactory(id, entityFactory):
        EntityFactory.factories[id] = entityFactory

    @staticmethod
    def createEntity(id):
        """A Template Method"""
        if id not in EntityFactory.factories:
            EntityFactory.factories[id] = eval(id + '.Factory()')
        return EntityFactory.factories[id].create()
