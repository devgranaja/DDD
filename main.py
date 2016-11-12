from entity import Entity, EntityFactory
from unique_id import UniqueId
from value import Value


class DireccionValueObject(Value):

    def __init__(self, value):
        super().__init__(value)
        self._direccion = value

    def __str__(self):
        return str(self._direccion)

    @property
    def direccion(self):
        return self._direccion


class PersonaEntity(Entity):

    def __init__(self, id):
        super().__init__(id)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str):
            self._nombre = value
        else:
            raise Exception("El nombre solo puede ser de tipo texto")

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        if isinstance(value, str):
            self._apellidos = value
        else:
            raise Exception("Los apellidos solo pueden ser de tipo texto")

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        if isinstance(value, DireccionValueObject):
            self._direccion = value
        else:
            raise Exception("La direccion solo puede ser de tipo Direccion")

    def nombre_completo(self):
        return self._nombre + " " + self._apellidos

    def __str__(self):
        return '{"persona":{"nombre":"%s", "apellidos":"%s", "direccion":"%s"}}' %\
               (self._nombre, self._apellidos, self._direccion)

    class Factory:
        @staticmethod
        def create():
            return PersonaEntity(UniqueId.id())


if __name__ == '__main__':
    EntityFactory.add_factory(PersonaEntity, PersonaEntity.Factory)

    persona = EntityFactory.create_entity(PersonaEntity)
    persona.nombre = "JAVIER"
    persona.apellidos = "AZUCAR MORENO"
    persona.direccion = DireccionValueObject("C/ Gustavo Adolfo Becquer")

    print(persona)

    pass
