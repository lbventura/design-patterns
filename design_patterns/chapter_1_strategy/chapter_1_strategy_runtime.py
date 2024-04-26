# The biggest difference between the Duck class in this module and in 'chapter_1_strategy.py'
# is that the Duck class accepts the flyBehavior and quackBehavior parameters at runtime.
# Therefore, we avoid the need for the setter methods set_fly_behavior and set_quack_behavior.

class FlyBehavior:
    @classmethod
    def fly(cls):
        raise NotImplementedError


class QuackBehavior:
    @classmethod
    def quack(cls):
        raise NotImplementedError


class Duck:
    def __init__(self, flyBehavior: FlyBehavior, quackBehavior: QuackBehavior):
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior

    def perform_fly(self):
        return self.flyBehavior.fly()

    def perform_quack(self):
        return self.quackBehavior.quack()

    @classmethod
    def swim(cls):
        return "All ducks swim, even decoy ducks!"


class FlyWithWings(FlyBehavior):
    @classmethod
    def fly(cls):
        return "An actual flight!"


class Quack(QuackBehavior):
    @classmethod
    def quack(cls):
        return "An actual quack!"


class MallardDuck(Duck):
    @classmethod
    def display(cls):
        return "I am a real Mallard duck!"


if __name__ == '__main__':
    print("Duck")
    duck = Duck(flyBehavior=FlyBehavior(), quackBehavior=QuackBehavior())
    print(duck.swim())

    print("Mallard Duck")
    mallard_duck = MallardDuck(flyBehavior=FlyWithWings(), quackBehavior=Quack())
    print(mallard_duck.perform_fly())
    print(mallard_duck.perform_quack())
    print(mallard_duck.swim())
    print(mallard_duck.display())
