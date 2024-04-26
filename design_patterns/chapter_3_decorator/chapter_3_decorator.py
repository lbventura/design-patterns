# The decorator pattern attaches additional responsibilities to an object dynamically,
# thereby providing a flexible alternative to subclassing when one wants to extend a class' functionality.
# In the example below, instances of the Beverage class get decorated with instances of CondimentDecorator
# thereby allowing a modification of Beverage.description, but also an extension of functionality (for example,
# with the method Whip.get_whip).

# Note: Inheritance is used to achieve *type matching* and NOT to get behavior.
# When we compose a decorator with a component, we are adding new behavior:
# this comes in through the composition of decorators with the base components as well as other decorators.

def _size_to_multiplier(size: str) -> float:
    if size == 'S':
        return 1.
    elif size == 'M':
        return 1.5
    elif size == 'L':
        return 2.
    else:
        raise ValueError("The selected value is not supported.")


class Beverage:
    description: str = "Unknown Beverage"
    size: str = "S"
    multiplier: float = 1.

    @classmethod
    def get_description(cls) -> str:
        return cls.description

    @classmethod
    def cost(cls) -> float:
        raise NotImplementedError

    @classmethod
    def set_size(cls, size: str) -> None:
        cls.size = size
        cls.multiplier = _size_to_multiplier(size=size)

    @classmethod
    def get_size(cls) -> str:
        return cls.size

    @classmethod
    def get_multiplier(cls) -> float:
        return cls.multiplier


class CondimentDecorator(Beverage):

    @classmethod
    def get_description(cls) -> str:
        return cls.description


class Expresso(Beverage):
    description: str = "Expresso"

    @classmethod
    def cost(cls) -> float:
        return 1.99 * cls.get_multiplier()


class HouseBlend(Beverage):
    description: str = "House Blend Coffee"

    @classmethod
    def cost(cls) -> float:
        return 0.89 * cls.get_multiplier()


class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        # the concrete decorator has an instance variable for the component the decorator is wrapping.
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        base_price = 0.20
        return self.beverage.cost() + base_price * self.beverage.get_multiplier()

    @staticmethod
    def get_mocha() -> str:
        return "Mochaccinos are the cutest!"


class Soy(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Soy'

    def cost(self):
        base_price = 0.15
        return self.beverage.cost() + base_price * self.beverage.get_multiplier()


class Whip(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        base_price = 0.10
        return self.beverage.cost() + base_price * self.beverage.get_multiplier()

    @staticmethod
    def get_whip() -> str:
        return "Whip it baby, ooh, whip it right!"


if __name__ == '__main__':
    # because Whip, Soy and Mocha (i.e., the decorators, which are instances of CondimentDecorator)
    # have the same supertype as Expresso (i.e., Beverage), they can be used multiple times.
    whip_soy_mocha_expresso = Whip(Soy(Mocha(Expresso())))
    assert "Expresso, Mocha, Soy, Whip" == whip_soy_mocha_expresso.get_description()
    assert isinstance(whip_soy_mocha_expresso.beverage, Soy)
    assert isinstance(whip_soy_mocha_expresso.beverage.beverage, Mocha)
    assert isinstance(whip_soy_mocha_expresso.beverage.beverage.beverage, Expresso)
    assert whip_soy_mocha_expresso.get_whip() == "Whip it baby, ooh, whip it right!"

    print("New drink coming up!")
    medium_expresso = Expresso()
    medium_expresso.set_size(size="M")
    assert "M" == medium_expresso.get_size()
    assert 1.5 == medium_expresso.get_multiplier()
