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
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        base_price = 0.20
        return self.beverage.cost() + base_price * self.beverage.get_multiplier()

    def get_mocha(self) -> str:
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

    def get_whip(self) -> str:
        return "Whip it baby, ooh, whip it right!"


if __name__ == '__main__':
    whip_soy_mocha_expresso = Whip(Soy(Mocha(Expresso())))
    assert "Expresso, Mocha, Soy, Whip" == whip_soy_mocha_expresso.get_description()
    assert isinstance(whip_soy_mocha_expresso.beverage, Soy)
    assert isinstance(whip_soy_mocha_expresso.beverage.beverage, Mocha)

    print("New drink coming up!")
    medium_expresso = Expresso()
    medium_expresso.set_size(size="M")
    assert "M" == medium_expresso.get_size()
    assert 1.5 == medium_expresso.get_multiplier()
