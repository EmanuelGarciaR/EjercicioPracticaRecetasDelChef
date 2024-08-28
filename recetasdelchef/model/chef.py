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

    def agregar_ingrediente(self, alimento: str, cantidad: float, unidad: UnidadMedida):
        ingrediente = Ingrediente(alimento, cantidad, unidad)
        self.ingredientes.append(ingrediente)

    def __str__(self):
        ingredientes_str = "\n".join(str(ingrediente) for ingrediente in self.ingredientes)
        return f"Receta {self.nombre}\nIngredientes:\n{ingredientes_str}\n\nDescripción:{self.descripcion}"
# TODO: Implementar la clase Chef
class Chef:
    def __init__(self):
        self.recetas: list[Receta] =  []
    def registrar_receta(self, nombre: str, ingredientes: list[tuple[str,float,UnidadMedida]], descripcion:  str, etiquetas: list[str]=None):
        receta = Receta(nombre, descripcion,etiquetas)
        for alimento, cantidad, unidad in ingredientes:
            receta.agregar_ingrediente(alimento, cantidad, unidad)
        self.recetas.append(receta)

    def buscar_receta(self, nombre: str)->Receta|None:
        for receta in self.recetas:
            if nombre.lower() in receta.nombre.lower():
                return receta
        return None

    def recetas_vegetarianas(self) ->list[Receta]:
        vegetarianas = []
        for receta in self.recetas:
            if "vegetariano" in receta.etiquetas or "VEGETARIANO" in receta.etiquetas:
                vegetarianas.append(receta)
        return vegetarianas

    def recetas_veganas(self) ->list[Receta]:
        veganas = []
        for  receta  in self.recetas:
            if "vegano"  in receta.etiquetas or "VEGANO"  in receta.etiquetas:
                veganas.append(receta)
        return veganas

