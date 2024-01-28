from typing import Optional


class Order:
    def __init__(self, beverage: Optional[str] = None, food: Optional[str] = None):
        if (beverage is None) and (food is None):
            raise ValueError("The customer is not ready to order.")

        self.beverage = beverage
        self.food = food
        self.ready = False

    def set_ready(self) -> None:
        self.ready = True


class Customer:
    def __init__(self):
        self.order = None

    def set_order(self, **kwargs) -> None:
        self.order = Order(**kwargs)


class Cook:

    @classmethod
    def cook_order(cls, order: Order) -> None:
        print(f"Preparing beverage {order.beverage} and food {order.food}")
        order.set_ready()
        print(f"Order is done!")


class Waiter:
    order_slips: dict = {}

    @classmethod
    def take_order(cls, customer: Customer) -> None:
        if customer.order is not None:
            cls.order_slips[customer] = customer.order

    @classmethod
    def order_up(cls, cook: Cook) -> None:
        for order in cls.order_slips.values():
            if not order.ready:
                cook.cook_order(order)

    @classmethod
    def get_order_slips(cls) -> dict:
        return cls.order_slips


if __name__ == '__main__':
    customer_1 = Customer()
    customer_1.set_order(beverage='Cola', food='Burger & Fries')
    print(customer_1.order)

    waiter = Waiter()
    waiter.take_order(customer=customer_1)
    print(waiter.get_order_slips())

    customer_2 = Customer()
    customer_2.set_order(beverage='Lemonade', food='Apple Pie')
    waiter.take_order(customer=customer_2)
    print(waiter.get_order_slips())

    angry_cook = Cook()
    waiter.order_up(cook=angry_cook)
    print(customer_1.order.ready)
    print(customer_2.order.ready)

    customer_3 = Customer()
    customer_3.set_order(beverage="Vanilla Milkshake")
    waiter.take_order(customer=customer_3)
    waiter.order_up(cook=angry_cook)
    print(customer_3.order.ready)

    customer_4 = Customer()
    customer_4.set_order(beverage="English Breakfast")
    print(waiter.get_order_slips())
    # there is actually nothing new to order because the waiter did not take customer 4
    # English Breakfast request
    waiter.order_up(cook=angry_cook)
    # this should then print False
    print(customer_4.order.ready)

    # should raise a ValueError because the customer has not ordered anything
    customer_5 = Customer()
    customer_5.set_order()
