# This example combines the Adapter, Decorator, Abstract Factory, Composite and Observer patterns.
# For more details, see pages 523-525 of the book.

from typing import List


class Observer:
    @classmethod
    def update(cls) -> None:
        raise NotImplementedError


class QuackObservable:

    @classmethod
    def register_observer(cls, observer: Observer) -> None:
        raise NotImplementedError

    @classmethod
    def notify_observers(cls) -> None:
        raise NotImplementedError


class Observable(QuackObservable):

    def __init__(self, duck: QuackObservable):
        self.duck = duck
        self.observers: list = []

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.update(self.duck)


class Quackologist(Observer):

    @classmethod
    def update(cls, duck: QuackObservable) -> None:
        print(f"I am a quackologist and this {str(duck)} just quacked!")


class Quackable(QuackObservable):
    def __init__(self):
        self.observable = Observable(duck=self)

    def __str__(self) -> str:
        return self.__class__.__name__

    @classmethod
    def quack(cls):
        raise NotImplementedError


class MallardDuck(Quackable):

    def quack(self):
        print("Quack!")
        self.notify_observers()

    def register_observer(self, observer: Observer) -> None:
        self.observable.register_observer(observer)

    def notify_observers(self) -> None:
        self.observable.notify_observers()


class ReadheadDuck(Quackable):
    @classmethod
    def quack(cls):
        print("Quaack!")


class DuckCall(Quackable):
    @classmethod
    def quack(cls):
        print("Kwak!")


class RubberDuck(Quackable):
    @classmethod
    def quack(cls):
        print("Squeak!")


class Goose:

    @classmethod
    def honk(cls):
        print("Honk!")


class GooseAdapter(Quackable):
    # Adapter Pattern, note that Ducks are of type Quackable.

    def __init__(self, goose: Goose):
        super().__init__()
        self.goose = goose

    def quack(self):
        self.goose.honk()


def counter(function):
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return function(*args, **kwargs)

    wrapper.num_calls = 0
    wrapper.__name__ = function.__name__
    return wrapper


class QuackCounter(Quackable):
    # Decorator Pattern

    def __init__(self, duck: Quackable):
        super().__init__()
        self.duck = duck

    # see also page 220 of Slatkin's "Effective Python"
    @counter
    def quack(self):
        self.duck.quack()

    def register_observer(self, observer: Observer) -> None:
        self.duck.observable.register_observer(observer)

    def notify_observers(self) -> None:
        self.duck.observable.notify_observers()


class AbstractDuckFactory:

    @classmethod
    def create_mallard_duck(cls):
        raise NotImplementedError

    @classmethod
    def create_redhead_duck(cls):
        raise NotImplementedError

    @classmethod
    def create_duck_call(cls):
        raise NotImplementedError

    @classmethod
    def create_rubber_duck(cls):
        raise NotImplementedError

    @classmethod
    def create_goose_duck(cls):
        raise NotImplementedError


class CountingDuckFactory(AbstractDuckFactory):
    # Factory Pattern

    @classmethod
    def create_mallard_duck(cls) -> Quackable:
        return QuackCounter(MallardDuck())

    @classmethod
    def create_redhead_duck(cls) -> Quackable:
        return QuackCounter(ReadheadDuck())

    @classmethod
    def create_duck_call(cls) -> Quackable:
        return QuackCounter(DuckCall())

    @classmethod
    def create_rubber_duck(cls) -> Quackable:
        return QuackCounter(RubberDuck())

    @classmethod
    def create_goose_duck(cls) -> Quackable:
        return GooseAdapter(Goose())


class Flock(Quackable):
    # Composite Pattern
    def __init__(self):
        super().__init__()
        self.quackers: list = []

    def add(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def register_observer(self, observer: Observer) -> None:
        for quacker in self.quackers:
            quacker.register_observer(observer)


class DuckSimulator:

    def __init__(self, duck_factory: AbstractDuckFactory, observers: List[Observer]):
        self.duck_factory = duck_factory
        self.observers = observers

    def simulate(self) -> None:
        redhead_duck = self.duck_factory.create_redhead_duck()
        duck_call = self.duck_factory.create_duck_call()
        rubber_duck = self.duck_factory.create_rubber_duck()
        goose_duck = self.duck_factory.create_goose_duck()

        flock_of_ducks = Flock()
        flock_of_ducks.add(redhead_duck)
        flock_of_ducks.add(duck_call)
        flock_of_ducks.add(rubber_duck)
        flock_of_ducks.add(goose_duck)

        self.simulate_duck(quackable=flock_of_ducks)

        flock_of_mallards = Flock()
        for _ in range(5):
            flock_of_mallards.add(self.duck_factory.create_mallard_duck())

        for observer in self.observers:
            flock_of_mallards.register_observer(observer)

        flock_of_ducks.add(flock_of_mallards)
        self.simulate_duck(quackable=flock_of_ducks)

        print(f"The total number of quacks is {rubber_duck.quack.num_calls}")

    @staticmethod
    def simulate_duck(quackable: Quackable):
        quackable.quack()


if __name__ == '__main__':
    ds = DuckSimulator(duck_factory=CountingDuckFactory(), observers=[Quackologist()])
    ds.simulate()
