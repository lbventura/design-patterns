# The template method pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
# This pattern lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
# Most importantly:
# * The methods which are specific are implemented in the subclasses;
# * The methods which are general are implemented in the parent class;

class CaffeineBeverage:

    @classmethod
    def prepare_recipe(cls):
        # this is the template method
        cls.boil_water()
        cls.brew()
        cls.pour_in_cup()
        cls.add_condiments()

    @classmethod
    def brew(cls):
        raise NotImplementedError

    @classmethod
    def add_condiments(cls):
        raise NotImplementedError

    @classmethod
    def boil_water(cls) -> None:
        print("Boiling water!")

    @classmethod
    def pour_in_cup(cls) -> None:
        print("Pouring drink into cup.")


class Coffee(CaffeineBeverage):
    # Note that Coffee does not call the abstract class without being called first
    # i.e.; users will interact with these classes through the template method,
    # `prepare_recipe`, which is called in CaffeineBeverage, which then delegates
    # to the child classes for concrete implementations.

    @classmethod
    def brew(cls) -> None:
        print("Brewing the coffee")

    @classmethod
    def add_condiments(cls) -> None:
        print("Adding sugar and milk")


class Tea(CaffeineBeverage):

    @classmethod
    def brew(cls) -> None:
        print("Steeping the tea")

    @classmethod
    def add_condiments(cls) -> None:
        print("Adding lemon")


class VehicleRevision:

    @classmethod
    def revise_vehicle(cls):
        cls.change_filter()
        cls.change_oil()
        cls.change_tires()
        cls.align_headlights()

        if cls.customer_wants_break_change():
            cls.change_breaks()

    @classmethod
    def change_filter(cls):
        print("Change filter")

    @classmethod
    def change_oil(cls):
        print("Change oil")

    @classmethod
    def change_tires(cls):
        raise NotImplementedError

    @classmethod
    def align_headlights(cls):
        print("Align headlights")

    @classmethod
    def change_breaks(cls):
        print("Change front breaks")

    # the direct hook implementation in Python looks rather odd
    @classmethod
    def customer_wants_break_change(cls):
        return False


class CarRevision(VehicleRevision):

    @classmethod
    def change_tires(cls):
        print("Changing 4 tires to new ones")

    @classmethod
    def customer_wants_break_change(cls):
        # car customers want to change breaks because
        # in their case it is not very expensive
        return True


class TruckRevision(VehicleRevision):

    @classmethod
    def change_tires(cls):
        print("Changing 6 tires to new ones")


if __name__ == '__main__':
    # caffeine beverage example
    coffee = Coffee()
    coffee.prepare_recipe()

    tea = Tea()
    tea.prepare_recipe()

    # vehicle revision example
    car_revision = CarRevision()
    car_revision.revise_vehicle()

    truck_revision = TruckRevision()
    truck_revision.revise_vehicle()
