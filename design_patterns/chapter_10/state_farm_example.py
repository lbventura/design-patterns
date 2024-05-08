# A silly example of the State pattern using
# a farm animal chorus

class Animal:

    def sing(self):
        pass


class NoAnimal(Animal):
    pass


class FarmAnimalChorus:

    def __init__(self):
        self.bass: Animal = Pig(farm_animal_chorus=self)
        self.soprano: Animal = Horse(farm_animal_chorus=self)
        self.alto: Animal = Donkey(farm_animal_chorus=self)
        self.end: Animal = NoAnimal()

        self.state = self.bass

    def set_state(self, state: Animal):
        self.state = state

    def sing(self):
        while not isinstance(self.state, NoAnimal):
            self.state.sing()


class Pig(Animal):

    def __init__(self, farm_animal_chorus: FarmAnimalChorus):
        self.farm_animal_chorus = farm_animal_chorus

    def sing(self) -> None:
        print("Oink, Oink!")
        self.farm_animal_chorus.set_state(state=self.farm_animal_chorus.soprano)


class Horse(Animal):

    def __init__(self, farm_animal_chorus: FarmAnimalChorus):
        self.farm_animal_chorus = farm_animal_chorus

    def sing(self) -> None:
        print("Hiiiii!")
        self.farm_animal_chorus.set_state(state=self.farm_animal_chorus.alto)


class Donkey(Animal):

    def __init__(self, farm_animal_chorus: FarmAnimalChorus):
        self.farm_animal_chorus = farm_animal_chorus

    def sing(self) -> None:
        print("Hi ho!")
        self.farm_animal_chorus.set_state(state=self.farm_animal_chorus.end)
        print("The chorus finishes after this animal")


if __name__ == '__main__':
    fac = FarmAnimalChorus()
    fac.sing()
