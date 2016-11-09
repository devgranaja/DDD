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
        self._id = uuid.uuid4().hex


    def __eq__(self, ent):
        return self._id == ent.id


    @property
    def id(self):
        """A string unique identifier for the entity."""
        return self._id


