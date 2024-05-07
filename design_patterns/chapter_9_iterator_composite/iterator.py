# The iterator pattern provides a way to access the elements of an aggregate object sequentially
# without exposing its underlying representation.

from typing import List


class MenuItem:

    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def get_price(self) -> float:
        return self.price


class Menu:

    @classmethod
    def create_iterator(cls):
        raise NotImplementedError


class Iterator:

    @classmethod
    def has_next(cls) -> bool:
        raise NotImplementedError

    @classmethod
    def next(cls) -> MenuItem:
        raise NotImplementedError


class PancakeHouseMenuIterator(Iterator):
    # Implements the details particular to the dataclass used in PancakeHouseMenu to register menu_items
    # e.g., a list

    def __init__(self, items: list):
        self.items = items
        self.position: int = 0

    def next(self) -> MenuItem:
        menu_item: MenuItem = self.items[self.position]
        self.position += 1
        return menu_item

    def has_next(self) -> bool:
        if self.position >= len(self.items):
            return False
        else:
            return True


class PancakeHouseMenu(Menu):

    def __init__(self):
        self.menu_items: list = []
        self.add_item("K&B Pancake Breakfast", "", True, 2.99)
        self.add_item("Regular Pancake Breakfast", "", False, 2.99)
        self.add_item("Blueberry Pancakes", "", True, 3.49)
        self.add_item("Waffles", "", True, 3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item = MenuItem(name=name, description=description, vegetarian=vegetarian, price=price)
        self.menu_items.append(menu_item)

    def create_iterator(self) -> PancakeHouseMenuIterator:
        return PancakeHouseMenuIterator(items=self.menu_items)


class DinerMenuIterator(Iterator):
    # Implements the details particular to the dataclass used in DinerMenu to register menu_items
    # e.g., a dict

    def __init__(self, items: dict):
        self.items = items
        self.position: int = 0

    def next(self) -> MenuItem:
        menu_item: MenuItem = self.items.get(self.position)
        self.position += 1
        return menu_item

    def has_next(self) -> bool:
        if self.position >= len(self.items):
            return False
        else:
            return True


class DinerMenu(Menu):
    max_items = 6

    def __init__(self):
        self.number_of_items: int = 0
        self.menu_items: dict = {}
        self.add_item("Veggie BLT", "", True, 2.99)
        self.add_item("BLT", "", False, 2.99)
        self.add_item("Soup of the day", "", False, 3.29)
        self.add_item("Hot dog", "", False, 3.05)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        if self.number_of_items >= self.max_items:
            raise RuntimeError("Menu is full, no more items are supported.")

        menu_item = MenuItem(name=name, description=description, vegetarian=vegetarian, price=price)
        self.menu_items[self.number_of_items] = menu_item
        self.number_of_items += 1

    def create_iterator(self) -> DinerMenuIterator:
        return DinerMenuIterator(items=self.menu_items)


class Waitress:

    def __init__(self, menu_list: List[Menu]):
        self.menu_list = menu_list

    def print_all_menus(self) -> None:

        for i, menu in enumerate(self.menu_list):
            print(f"The items in the {i} menu are:")
            iterator = menu.create_iterator()
            self.print_menu(iterator=iterator)

    @staticmethod
    def print_menu(iterator: Iterator) -> None:

        while iterator.has_next():
            menu_item = iterator.next()
            print(f"The item's names is {menu_item.get_name()}: Vegetarian? {menu_item.is_vegetarian()}."
                  f" Price? {menu_item.get_price()}")


if __name__ == '__main__':
    waitress = Waitress(menu_list=[PancakeHouseMenu(), DinerMenu()])

    waitress.print_all_menus()

    diner_menu = DinerMenu()
    for _ in range(1, 10):
        diner_menu.add_item(name="Fake item", description="", vegetarian=False, price=0.)
        print(diner_menu.menu_items)
