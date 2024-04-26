from time import sleep
from typing import Optional


class Order:
    """Corresponds to Command in the class diagram.
    It is responsible for mediating between the Receiver (e.g.,
    the Cook) and the Client (e.g., the Customer)."""

    def __init__(self, beverage: Optional[str] = None, food: Optional[str] = None):
        if (beverage is None) and (food is None):
            raise ValueError("The customer is not ready to order.")

        self.beverage = beverage
        self.food = food
        self.ready = False

    def set_ready(self) -> None:
        self.ready = True

    def order_up(self, cook: "Cook") -> None:
        """Corresponds to `.execute()`, through the `cook_order` method."""
        cook.cook_order(beverage=self.beverage, food=self.food)
        self.set_ready()
        print(f"Order is done!")


class Customer:
    """This corresponds to the Client in the class diagram.
    It is responsible for creating the command object.
    The command object consists of a set of actions on a receiver.
    """

    def __init__(self):
        self.order = None

    def set_order(self, **kwargs) -> None:
        self.order = Order(**kwargs)


class Cook:
    """Corresponds to the Receiver in the class diagram."""

    @classmethod
    def cook_order(cls, beverage: str, food: str) -> None:
        print(f"Preparing beverage {beverage} and food {food}.")
        sleep(1)
        print(f"Preparation of {beverage} and {food} is done.")


class Waiter:
    """Corresponds to the Invoker in the class diagram.
    The Invoker holds a command (i.e., an Order) and at some point asks the command to carry out a request by calling
    the corresponding `.execute()` method"""

    def __init__(self):
        self.order_slips: dict = {}

    def take_order(self, customer: Customer) -> None:
        """This corresponds to set_command() in the class diagram."""
        if customer.order is not None:
            self.order_slips[customer] = customer.order

    def get_order_slips(self) -> dict:
        return self.order_slips

    def remove_order(self, customer: Customer) -> None:
        self.order_slips.pop(customer, None)

    def execute(self, cook: Cook):
        """The coupling between Waiter and Cook only happens here because the Waiter can select which Cook to give
        the order to."""
        for order in self.order_slips.values():
            order.order_up(cook=cook)


if __name__ == '__main__':
    customer_1 = Customer()
    customer_1.set_order(beverage='Cola', food='Burger & Fries')

    waiter = Waiter()
    waiter.take_order(customer=customer_1)
    print(waiter.get_order_slips())

    customer_2 = Customer()
    customer_2.set_order(beverage='Lemonade', food='Apple Pie')
    waiter.take_order(customer=customer_2)
    print(waiter.get_order_slips())

    angry_cook = Cook()
    waiter.execute(cook=angry_cook)
    print(customer_1.order.ready)
    print(customer_2.order.ready)

    customer_3 = Customer()
    customer_3.set_order(beverage="Vanilla Milkshake")
    waiter.take_order(customer=customer_3)
    waiter.execute(cook=angry_cook)
    print(customer_3.order.ready)

    customer_4 = Customer()
    customer_4.set_order(beverage="English Breakfast")
    print(waiter.get_order_slips())
    # there is actually nothing new to order because the waiter did not take customer 4
    # English Breakfast request
    waiter.execute(cook=angry_cook)
    # this should then print False
    print(customer_4.order.ready)

    # should raise a ValueError because the customer has not ordered anything
    customer_5 = Customer()
    customer_5.set_order()
