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


class PancakeHouseMenu:

    def __init__(self):
        self.menu_items: list = []
        self.add_item("K&B Pancake Breakfast", "", True, 2.99)
        self.add_item("Regular Pancake Breakfast", "", False, 2.99)
        self.add_item("Blueberry Pancakes", "", True, 3.49)
        self.add_item("Waffles", "", True, 3.59)

    def add_item(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        menu_item = MenuItem(name=name, description=description, vegetarian=vegetarian, price=price)
        self.menu_items.append(menu_item)

    def get_menu_items(self) -> list:
        return self.menu_items


class DinerMenu:
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

    def get_menu_items(self) -> dict:
        return self.menu_items


class Waitress:

    @staticmethod
    def print_breakfast_menu():
        breakfast_menu = PancakeHouseMenu()
        breakfast_items = breakfast_menu.get_menu_items()

        for index, menu_item in enumerate(breakfast_items):
            print(f"Item no {index}")
            print(f"The item's names is {menu_item.get_name()}: Vegetarian? {menu_item.is_vegetarian()}."
                  f" Price? {menu_item.get_price()}")

    @staticmethod
    def print_lunch_menu():
        lunch_menu = DinerMenu()
        lunch_items = lunch_menu.get_menu_items()

        for index in lunch_items.keys():
            print(f"Item no {index}")
            menu_item = lunch_items.get(index)
            print(f"The item's names is {menu_item.get_name()}: Vegetarian? {menu_item.is_vegetarian()}."
                  f" Price? {menu_item.get_price()}")


if __name__ == '__main__':
    waitress = Waitress()

    waitress.print_breakfast_menu()

    waitress.print_lunch_menu()
