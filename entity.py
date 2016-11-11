import uuid


# ======================================================================================================================
# Entities
#

class Entity:
    """The base class of all entities.

    Attributes:
        id: A unique identifier.
    """

    def __init__(self):
        """Initialize a Entity.

        Do NOT call directly. Use the factory method.
        """
        pass

    def __eq__(self, ent):
        return self._id == ent.id

    @property
    def id(self):
        """A string unique identifier for the entity."""
        return self._id

    @staticmethod
    def factory():
        """Factory method."""
        obj = Entity()
        obj._id = uuid.uuid4().hex
        return obj
