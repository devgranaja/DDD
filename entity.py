

# ======================================================================================================================
# Entities
#
class Entity(object):
    """The base class of all entities.
    Attributes:
        id: A unique identifier.
    """

    def __init__(self, id):
        """Initialize a Entity.

        Do NOT call directly. Use the factory class.
        """
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
    def add_factory(entity, entity_factory):
        entity_name = entity.__name__
        EntityFactory.factories[entity_name] = entity_factory

    @staticmethod
    def create_entity(entity):
        """A Template Method"""
        entity_name = entity.__name__
        if entity_name not in EntityFactory.factories:
            EntityFactory.factories[entity_name] = eval(entity_name + '.Factory()')
        return EntityFactory.factories[entity_name].create()
