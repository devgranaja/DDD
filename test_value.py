import pytest
from value import Value


class ValueString(Value):
    def __init__(self, s):
        self.param = s


class ValueOtherString(Value):
    def __init__(self, os):
        self.param = os


class ValueInt(Value):
    def __init__(self, i):
        self.par = i


class ValueIntInheritance(ValueInt):
    pass


@pytest.fixture
def value_object_string1():
    obj = ValueString("value1")
    return obj


@pytest.fixture
def value_object_string1bis():
    obj = ValueString("value1")
    return obj


@pytest.fixture
def value_object_string2():
    obj = ValueString("value2")
    return obj


@pytest.fixture
def value_object_other_string():
    obj = ValueOtherString("value1")
    return obj


@pytest.fixture
def value_object_int():
    obj = ValueInt(18)
    return obj


@pytest.fixture
def value_object_int2():
    obj = ValueInt(18)
    return obj


@pytest.fixture
def value_object_int_inheritance():
    obj = ValueIntInheritance(18)
    return obj

def test_equality_string_objs(value_object_string1, value_object_string1bis):
    assert value_object_string1 == value_object_string1bis


def test_equality_string_obj1_obj2(value_object_string1, value_object_string2):
    assert value_object_string1 != value_object_string2


def test_equality_dif_class(value_object_string1, value_object_other_string):
    assert value_object_string1 != value_object_other_string


def test_equality_dif_params(value_object_int, value_object_int2):
    assert value_object_int == value_object_int2


def test_equalitiy_inheritance(value_object_int, value_object_int_inheritance):
    print("pi2\n")
    assert value_object_int != value_object_int_inheritance
