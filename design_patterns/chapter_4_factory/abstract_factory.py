# Because instantiating objects can lead to coupling problems, the factory pattern defines an interface for creating
# an object, while letting subclasses decide which objects to instantiate.
# The abstract factory pattern provides an interface for creating **families** of related or dependent objects without
# specifying their concrete classes.

# Both Factory Method and Abstract Factory create objects, but the former does it through *inheritance*
# (i.e, extend a class and override a factory method, in our case `create_pizza`.
# The inheritance in this case can be seen at the level of dough, sauce and toppings)
# and the latter through *object composition*.

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
        """
        Note that `order_pizza` is defined in the class, not in the subclass.
        Therefore, this method has no idea which subclass is actually running the code and making the pizzas.
        It is the subclasses of `PizzaStore` that handle object instantiation for us in the `create_pizza` method.

        :param pizza_type:
        :return:
        """
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
    """This abstract interface defines how to make a family of related products (e.g., the ingredients).
    The disadvantage here is that one would need to add a new method here (and to the corresponding) subclasses
    if a new ingredient (for example, pineapple) was added."""

    @classmethod
    def create_dough(cls):
        """Each ingredient represents a product produced by a Factory Method in the Abstract Factory."""
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


class NYPizzaStore(PizzaStore):
    """The factory method `create_pizza` is implemented in the concrete subclass of PizzaStore, NYPizzaStore.
    It is this factory method that is responsible for instantiation."""

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        # this is where the object composition happens
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
