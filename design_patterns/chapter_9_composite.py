class MenuComponent:

    @classmethod
    def get_name(cls):
        raise NotImplementedError

    @classmethod
    def get_description(cls):
        raise NotImplementedError

    @classmethod
    def get_price(cls):
        raise NotImplementedError

    @classmethod
    def is_vegetarian(cls):
        raise NotImplementedError

    @classmethod
    def print(cls):
        raise NotImplementedError

    @classmethod
    def add(cls, menu_component: object):
        raise NotImplementedError

    @classmethod
    def remove(cls, menu_component: object):
        raise NotImplementedError

    @classmethod
    def get_child(cls, i: int):
        raise NotImplementedError


class MenuItem(MenuComponent):

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

    def print(self) -> None:
        print(f"The item's names is {self.get_name()}: Vegetarian? {self.is_vegetarian()}."
              f" Price? {self.get_price()}")


class Menu(MenuComponent):

    def __init__(self, name: str, description: str):
        self.menu_components = []
        self.name = name
        self.description = description

    def add(self, menu_component: MenuComponent) -> None:
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent) -> None:
        menu_component_index = self.menu_components.index(menu_component)
        self.menu_components.pop(menu_component_index)

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def print(self) -> None:
        print(f"The menu's names is {self.get_name()}."
              f" Description? {self.get_description()}")

        for ele in self.menu_components:
            ele.print()


class Waitress:

    def __init__(self, menus: MenuComponent):
        self.menus = menus

    def print_menu(self) -> None:
        self.menus.print()


if __name__ == '__main__':

    pancake_house_menu = Menu("Pancake House", "Breakfast")
    diner_menu = Menu("Diner", "Lunch")
    cafe_menu = Menu("Cafe", "Dinner")
    dessert_menu = Menu("Dessert", "Dessert")

    all_menus = Menu("ALL MENUS", "All Menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    steak_fries = MenuItem("Steak Fries", "Steak with a side of fries", False, 6.99)
    cafe_menu.add(steak_fries)

    cafe_menu.add(dessert_menu)
    banana_split = MenuItem("Banana Split", "", True, 2.99)
    dessert_menu.add(banana_split)

    veggie_item = MenuItem("Veggie BLT", "", True, 2.99)
    diner_menu.add(veggie_item)

    waitress = Waitress(menus=all_menus)
    waitress.print_menu()
