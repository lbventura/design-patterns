from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str):
        self.value = value


def test_singleton(value: str) -> None:
    singleton = Singleton(value=value)
    print(f"Object {singleton}, id: {id(singleton)}")
    print(singleton.value)


if __name__ == '__main__':
    process_1 = Thread(target=test_singleton, args=('First_value', ))
    process_2 = Thread(target=test_singleton, args=('This value should not be printed', ))

    process_1.start()
    process_2.start()
