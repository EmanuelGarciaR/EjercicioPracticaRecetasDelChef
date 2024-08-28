from enum import StrEnum


class UnidadMedida(StrEnum):
    GRAMO = "gr"
    KILOGRAMO = "kg"
    LITRO = "l"
    MILILITRO = "ml"
    TAZA = "taza"
    CUCHARADA = "cda"
    CUCHARADITA = "cdita"
    UNIDAD = "unidad"

    @classmethod
    def list(cls) -> list[str]:
        return list(map(lambda c: c.value, cls))


# TODO: Implementar la clase Ingrediente
class Ingrediente:
    def __init__(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        self.alimento: str = alimento
        self.cantidad: float = cantidad
        self.unidad: UnidadMedida = unidad

    def __str__(self):
        return f"{self.cantidad} {self.unidad.value} de {self.alimento}"
# TODO: Implementar la clase Receta

class Receta:
    def __init__(self, nombre: str, descripcion:  str, etiquetas: list[str] = None):
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.ingredientes: list[Ingrediente] = []
        self.etiquetas: list[str] = etiquetas if etiquetas is not None else []


# TODO: Implementar la clase Chef
