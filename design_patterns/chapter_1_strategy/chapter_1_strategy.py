# The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# Strategy lets the algorithm vary independently of clients that use it.
# This is convenient because different users can share the same code.
# In the example below, Icarus and RocketMan (i.e, the users) use the same FlyBehavior as Duck.


class FlyBehavior:
    @classmethod
    def fly(cls):
        raise NotImplementedError


class QuackBehavior:
    @classmethod
    def quack(cls):
        raise NotImplementedError


class Duck:
    flyBehavior = FlyBehavior()
    quackBehavior = QuackBehavior()

    @classmethod
    def perform_fly(cls):
        return cls.flyBehavior.fly()

    @classmethod
    def perform_quack(cls):
        return cls.quackBehavior.quack()

    @classmethod
    def swim(cls) -> str:
        return "All ducks swim, even decoy ducks!"

    @classmethod
    def set_fly_behavior(cls, fly_behavior: FlyBehavior) -> None:
        cls.flyBehavior = fly_behavior

    @classmethod
    def set_quack_behavior(cls, quack_behavior: QuackBehavior) -> None:
        cls.quackBehavior = quack_behavior

    @classmethod
    def display(cls):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    """Implementation of FlyBehavior to perform a normal flight"""

    @classmethod
    def fly(cls) -> str:
        return "A normal flight!"


class FlyWithRocket(FlyBehavior):
    """Implementation of FlyBehavior to perform a ROCKET flight"""

    @classmethod
    def fly(cls) -> str:
        return "ROCKET FLIGHT!"


class Quack(QuackBehavior):
    """Implementation of QuackBehavior to perform a normal quack"""

    @classmethod
    def quack(cls) -> str:
        return "A normal quack!"


class MallardDuck(Duck):
    @classmethod
    def display(cls) -> str:
        return "I am a real Mallard duck!"


class Man:
    flyBehavior = FlyBehavior()

    @classmethod
    def perform_fly(cls):
        return cls.flyBehavior.fly()

    @classmethod
    def set_fly_behavior(cls, fly_behavior: FlyBehavior) -> None:
        cls.flyBehavior = fly_behavior

    @classmethod
    def sing(cls):
        raise NotImplementedError


class RocketMan(Man):

    @classmethod
    def sing(cls) -> str:
        return "'Cause I am rocket man!"


class Icarus(Man):

    @classmethod
    def sing(cls) -> str:
        return "I am flying close to the Sun!"


if __name__ == '__main__':
    print("Duck")
    duck = Duck()
    print(duck.swim())

    print("Mallard Duck")
    mallard_duck = MallardDuck()
    mallard_duck.set_fly_behavior(fly_behavior=FlyWithWings())
    print(mallard_duck.perform_fly())

    mallard_duck.set_quack_behavior(quack_behavior=Quack())
    print(mallard_duck.perform_quack())
    print(mallard_duck.swim())
    print(mallard_duck.display())

    mallard_duck.set_fly_behavior(fly_behavior=FlyWithRocket())
    print(mallard_duck.perform_fly())

    print("Rocket Man")
    rocket_man = RocketMan()
    print(rocket_man.sing())
    rocket_man.set_fly_behavior(fly_behavior=FlyWithRocket())
    print(rocket_man.perform_fly())

    print("Icarus")
    rocket_man = Icarus()
    print(rocket_man.sing())
    rocket_man.set_fly_behavior(fly_behavior=FlyWithWings())
    print(rocket_man.perform_fly())
