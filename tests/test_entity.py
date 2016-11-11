import pytest
from entity import Entity, EntityFactory
import uuid



class EntityTest1(Entity):
    def __init__(self, id):
        super().__init__(id)


class EntityTest2(Entity):
    def __init__(self, id):
        super().__init__(id)


class EntityTest3(Entity):
    def __init__(self, id):
        super().__init__(id)

    class Factory:
        @staticmethod
        def create():
            return EntityTest3(uuid.uuid4().hex)


@pytest.fixture
def entity_test1():
    obj = EntityTest1(uuid.uuid4().hex)
    return obj


@pytest.fixture
def entity_test1bis():
    obj = EntityTest1(uuid.uuid4().hex)
    return obj


@pytest.fixture
def entity_test2():
    obj = EntityTest2(uuid.uuid4().hex)
    return obj


@pytest.fixture
def entity_test3():
    EntityFactory.addFactory(EntityTest3.__name__, EntityTest3.Factory)
    obj = EntityFactory.createEntity(EntityTest3.__name__)
    return obj


def test_equality_entity_obj1(entity_test1):
    return entity_test1 == entity_test1


def test_dif_entity_obj1_obj1(entity_test1, entity_test1bis):
    assert entity_test1 != entity_test1bis


def test_dif_entity_obj1_obj2(entity_test1, entity_test2):
    assert entity_test1 != entity_test2


def test_factory_entity(entity_test3):
    assert True