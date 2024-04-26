# In the simple factory approach, the factory is another object composed with PizzaStore.

class Pizza:
    status: str = "Order"

    @classmethod
    def prepare(cls) -> None:
        print("Pizza is being prepared.")
        cls.status = "Prepare"

    @classmethod
    def bake(cls) -> None:
        print("Pizza is being baked.")
        cls.status = "Bake"

    @classmethod
    def cut(cls) -> None:
        print("Pizza is being cut.")
        cls.status = "Cut"

    @classmethod
    def box(cls) -> None:
        print("Pizza is being boxed.")
        cls.status = "Box"


class CheesePizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass


class SimplePizzaFactory:

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()
        elif pizza_type == "clam":
            pizza = ClamPizza()
        elif pizza_type == "veggie":
            pizza = VeggiePizza()
        else:
            raise ValueError(f"Pizza type {pizza_type} is not supported.")
        return pizza


class PizzaStore:
    """
    Implementation using SimplePizzaFactory. Here the factory (SimplePizzaFactory) is composed with PizzaStore.
    """
    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.factory.create_pizza(pizza_type=pizza_type)

        pizza.prepare()
        print(pizza.status)
        pizza.bake()
        print(pizza.status)
        pizza.cut()
        print(pizza.status)
        pizza.box()
        print(pizza.status)
        print("Pizza has been prepared!")
        return pizza


if __name__ == '__main__':
    pizza_factory = SimplePizzaFactory()

    first_order = pizza_factory.create_pizza(pizza_type="cheese")
    print(type(first_order))

    pizza_store = PizzaStore(factory=SimplePizzaFactory())
    order = pizza_store.order_pizza(pizza_type="clam")
