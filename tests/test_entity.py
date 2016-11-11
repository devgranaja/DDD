import pytest
from entity import Entity


class EntityTest1(Entity):
    def __init__(self):
        super().__init__()


class EntityTest2(Entity):
    def __init__(self):
        super().__init__()


@pytest.fixture
def entity_test1():
    obj = EntityTest1.factory()
    return obj


@pytest.fixture
def entity_test1bis():
    obj = EntityTest1.factory()
    return obj


@pytest.fixture
def entity_test2():
    obj = EntityTest2.factory()
    return obj


def test_equality_entity_obj1(entity_test1):
    return entity_test1 == entity_test1


def test_dif_entity_obj1_obj1(entity_test1, entity_test1bis):
    assert entity_test1 != entity_test1bis


def test_dif_entity_obj1_obj2(entity_test1, entity_test2):
    assert entity_test1 != entity_test2
