# The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# Strategy lets the algorithm vary independently of clients that use it.*


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


class WeaponBehavior:
    @classmethod
    def use_weapon(cls):
        raise NotImplementedError


class KnifeBehavior(WeaponBehavior):
    @classmethod
    def use_weapon(cls) -> str:
        return "Poke with staby stab!"


class Character:
    weapon = WeaponBehavior()

    @classmethod
    def fight(cls):
        return cls.weapon.use_weapon()

    @classmethod
    def set_weapon(cls, weapon: WeaponBehavior):
        cls.weapon = weapon


class Queen(Character):
    pass


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

    queen = Queen()
    queen.set_weapon(weapon=KnifeBehavior())
    print(queen.fight())
