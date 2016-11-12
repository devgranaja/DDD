import pytest
from entity import Entity, EntityFactory
from unique_id import UniqueId


class EntityTest1(Entity):
    def __init__(self, id):
        super().__init__(id)

    class Factory:
        @staticmethod
        def create():
            return EntityTest1(UniqueId.id())


class EntityTest2(Entity):
    def __init__(self, id):
        super().__init__(id)

    class Factory:
        @staticmethod
        def create():
            return EntityTest2(UniqueId.id())


class EntityTest3(Entity):
    def __init__(self, id):
        super().__init__(id)

    class Factory:
        @staticmethod
        def create():
            return EntityTest3(UniqueId.id())


@pytest.fixture
def entity_test1():
    EntityFactory.add_factory(EntityTest1, EntityTest1.Factory)
    obj = EntityFactory.create_entity(EntityTest1)
    return obj


@pytest.fixture
def entity_test1bis():
    EntityFactory.add_factory(EntityTest1, EntityTest1.Factory)
    obj = EntityFactory.create_entity(EntityTest1)
    return obj


@pytest.fixture
def entity_test2():
    EntityFactory.add_factory(EntityTest2, EntityTest2.Factory)
    obj = EntityFactory.create_entity(EntityTest2)
    return obj


@pytest.fixture
def entity_test3():
    EntityFactory.add_factory(EntityTest3, EntityTest3.Factory)
    obj = EntityFactory.create_entity(EntityTest3)
    return obj


def test_equality_entity_obj1(entity_test1):
    return entity_test1 == entity_test1


def test_dif_entity_obj1_obj1(entity_test1, entity_test1bis):
    assert entity_test1 != entity_test1bis


def test_dif_entity_obj1_obj2(entity_test1, entity_test2):
    assert entity_test1 != entity_test2
