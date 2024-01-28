from typing import List


class Pizza:

    def __init__(self, name: str, dough: str, sauce: str, toppings: List[str]):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings

    def prepare(self) -> None:
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Add sauce...")
        print("Add toppings")
        for topping in self.toppings:
            print(f"Add {topping}")

    def bake(self) -> None:
        print(f"Bake {self.name} for 25 minutes at 350.")

    def cut(self) -> None:
        print(f"Cut {self.name} in diagonal slices.")

    def box(self) -> None:
        print(f"Place {self.name} in the official store box.")


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


class NYCheesePizza(Pizza):

    def __init__(self):
        super().__init__(name="NY Style Sauce and Cheese Pizza", dough="Thin Crust", sauce="Marinara Sauce",
                         toppings=["Grated Reggiano Cheese"])


class NYPepperoniPizza(Pizza):
    def __init__(self):
        super().__init__(name="NY Style Pepperoni Pizza", dough="Thin Crust", sauce="Marinara Sauce with Basilicum",
                         toppings=["Grated Reggiano Cheese", "Parma Pepperoni"])


class NYClamPizza(Pizza):
    def __init__(self):
        super().__init__(name="NY Style Clam Pizza", dough="Thin Crust", sauce="Marinara Sauce with Oregano",
                         toppings=["Grated Reggiano Cheese", "Genova Clams"])


class NYVeggiePizza(Pizza):
    def __init__(self):
        super().__init__(name="NY Style Veggie Pizza", dough="Thin Crust", sauce="Marinara Sauce with Oregano",
                         toppings=["Grated Reggiano Cheese", "Neapolitan Aubergine"])


class NYPizzaStore(PizzaStore):

    @classmethod
    def create_pizza(cls, pizza_type: str) -> Pizza:
        if pizza_type == "cheese":
            pizza = NYCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = NYPepperoniPizza()
        elif pizza_type == "clam":
            pizza = NYClamPizza()
        elif pizza_type == "veggie":
            pizza = NYVeggiePizza()
        else:
            raise ValueError(f"Pizza type {pizza_type} is not supported.")
        return pizza


if __name__ == '__main__':
    print("Let us create a NY Pizza")
    pizza_store = NYPizzaStore()
    pizza_store.order_pizza(pizza_type="cheese")
