class AnimalFarm:

    # не очень понял прикола с фабрикой. Класс животного определяется при инициализации экзампляра фабрики
    # или должен был быть определен методом отдельно?
    def __init__(self, animal_type: str, **kwargs):
        match animal_type:
            case "Bird":
                self._animal = Bird(**kwargs)
            case "Fish":
                self._animal = Fish(**kwargs)
            case "Mammal":
                self._animal = Mammal(**kwargs)
            case _:
                self._animal = Animal(**kwargs)

    def get_animal(self):
        return self._animal


class Animal:

    def __init__(self, name: str = "", age: int = 1):
        self._name, self._age = name, age

    def __repr__(self):
        return f'{self._name}, {self._age}'


class Bird(Animal):

    def __init__(self, feathers: str = "Featherless", **kwargs):
        super().__init__(**kwargs)
        self._feathers = feathers

    def __repr__(self):
        return f'{super().__repr__()}, Feathers: {self._feathers}'


class Mammal(Animal):

    def __init__(self, fur: str = "No fur", **kwargs):
        super().__init__(**kwargs)
        self._fur = fur

    def __repr__(self):
        return f'{super().__repr__()}, Fur: {self._fur}'


class Fish(Animal):

    def __init__(self, scale_color: str = 'White', **kwargs):
        super().__init__(**kwargs)
        self._scale_color = scale_color

    def __repr__(self):
        return f'{super().__repr__()}, Scales: {self._scale_color}'


if __name__ == "__main__":
    nemo = Fish(scale_color='Orange', name='Nemo', age=3)
    print(nemo)
    fabric = AnimalFarm("Fish", name="Dory", age="5", scale_color="Blue")
    wonderland = AnimalFarm("unknown", name="Jabberwocky", age="1000")
    print(fabric.get_animal())
    print(wonderland.get_animal())
