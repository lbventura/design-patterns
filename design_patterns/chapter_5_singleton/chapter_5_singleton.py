# The singleton pattern ensures a class has only one instance and provides a global point of access to it.
# Avoid subclassing a Singleton!
# See https://refactoring.guru/design-patterns/singleton/python/example
from sys import _getframe


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    It is possible to initialize Singleton multiple times, but
    SingletonMeta guarantees that we obtain the same instance.

    This is not what is done in the Head First Design Patterns
    book, where only a single instance is ever instantiated.
    """
    pass


class HeadFirstSingleton:
    unique_instance = None

    def __init__(self):
        caller_name = _getframe(1).f_code.co_name
        if caller_name != "get_instance":
            raise Exception("This class should not be initialized outside get_instance.")

    @classmethod
    def get_instance(cls) -> "HeadFirstSingleton":
        if cls.unique_instance is None:
            cls.unique_instance = HeadFirstSingleton()
        return cls.unique_instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(f"Object {s1}, id: {id(s1)}")
    print(f"Object {s2}, id: {id(s2)}")
    print("As expected, both variables are referring to the same instance.")

    sj1 = HeadFirstSingleton.get_instance()
    sj2 = HeadFirstSingleton.get_instance()
    print(f"Object {sj1}, id: {id(sj1)}")
    print(f"Object {sj2}, id: {id(sj2)}")

    # this raises an Exception as defined above
    sj3 = HeadFirstSingleton()
