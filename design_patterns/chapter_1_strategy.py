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
    def set_fly_behavior(cls, fb) -> None:
        cls.flyBehavior = fb

    @classmethod
    def set_quack_behavior(cls, qb) -> None:
        cls.quackBehavior = qb


class FlyWithWings(FlyBehavior):
    @classmethod
    def fly(cls) -> str:
        return "An actual flight!"


class FlyWithRocket(FlyBehavior):
    @classmethod
    def fly(cls) -> str:
        return "ROCKET FLIGHT!"


class Quack(QuackBehavior):
    @classmethod
    def quack(cls) -> str:
        return "An actual quack!"


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
    def set_weapon(cls, wp):
        cls.weapon = wp


class Queen(Character):
    pass


if __name__ == '__main__':
    print("Duck")
    duck = Duck()
    print(duck.swim())

    print("Mallard Duck")
    mallard_duck = MallardDuck()
    mallard_duck.set_fly_behavior(fb=FlyWithWings())
    print(mallard_duck.perform_fly())
    mallard_duck.set_quack_behavior(qb=Quack())
    print(mallard_duck.perform_quack())
    print(mallard_duck.swim())
    print(mallard_duck.display())

    mallard_duck.set_fly_behavior(fb=FlyWithRocket())
    print(mallard_duck.perform_fly())

    queen = Queen()
    queen.set_weapon(wp=KnifeBehavior())
    print(queen.fight())
