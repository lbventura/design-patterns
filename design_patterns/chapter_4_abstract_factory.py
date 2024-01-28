class Dough:
    pass


class Sauce:
    pass


class Cheese:
    pass


class Veggies:
    pass


class Pepperoni:
    pass


class Clams:
    pass


class Pizza:
    name: str
    dough: Dough
    sauce: Sauce
    veggies: Veggies
    cheese: Cheese
    pepperoni: Pepperoni
    clams: Clams

    def prepare(self) -> None:
        raise NotImplementedError

    def bake(self) -> None:
        print(f"Bake {self.name} for 25 minutes at 350.")

    def cut(self) -> None:
        print(f"Cut {self.name} in diagonal slices.")

    def box(self) -> None:
        print(f"Place {self.name} in the official store box.")

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        print(f"The yummy pizza is {self.name}!")


class PizzaStore:
    @classmethod
    def order_pizza(cls, pizza_type: str) -> Pizza:
        pizza = cls.create_pizza(pizza_type=pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        raise NotImplementedError


class PizzaIngredientFactory:

    @classmethod
    def create_dough(cls):
        raise NotImplementedError

    @classmethod
    def create_sauce(cls):
        raise NotImplementedError

    @classmethod
    def create_cheese(cls):
        raise NotImplementedError

    @classmethod
    def create_veggies(cls):
        raise NotImplementedError

    @classmethod
    def create_pepperoni(cls):
        raise NotImplementedError

    @classmethod
    def create_clam(cls):
        raise NotImplementedError


class ThinCrustDough(Dough):
    pass


class MarinaraSauce(Sauce):
    pass


class ReggianoCheese(Cheese):
    pass


class SlicedPepperoni(Pepperoni):
    pass


class FreshClams(Clams):
    pass


class DicedVeggies(Veggies):
    pass


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class PepperoniPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clams = self.ingredient_factory.create_clam()


class VeggiePizza(Pizza):

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    @classmethod
    def create_dough(cls) -> Dough:
        return ThinCrustDough()

    @classmethod
    def create_sauce(cls) -> Sauce:
        return MarinaraSauce()

    @classmethod
    def create_cheese(cls) -> Cheese:
        return ReggianoCheese()

    @classmethod
    def create_veggies(cls) -> Veggies:
        return DicedVeggies()

    @classmethod
    def create_pepperoni(cls) -> Pepperoni:
        return SlicedPepperoni()

    @classmethod
    def create_clam(cls) -> Clams:
        return FreshClams()


class NYPizzaStore(PizzaStore):

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()

        if pizza_type == "cheese":
            pizza = CheesePizza(ingredient_factory=ingredient_factory)
            pizza.set_name("NY Style Cheese Pizza")
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory=ingredient_factory)
            pizza.set_name("NY Style Pep Pizza")
        elif pizza_type == "clam":
            pizza = ClamPizza(ingredient_factory=ingredient_factory)
            pizza.set_name("NY Style Clam Pizza")
        elif pizza_type == "veggie":
            pizza = VeggiePizza(ingredient_factory=ingredient_factory)
            pizza.set_name("NY Style Veggie Pizza")
        else:
            raise ValueError(f"Pizza type {pizza_type} is not supported.")
        return pizza


if __name__ == '__main__':
    print("Let us create a NY Pizza")
    pizza_store = NYPizzaStore()
    delivery_pizza = pizza_store.order_pizza(pizza_type="cheese")
    print(delivery_pizza.sauce)
