# The observer pattern defines a one-to-many dependency between objects so that when one object changes state,
# all of its dependents are notified and updated automatically.


import uuid
import random
from time import sleep


class Observer:

    def __init__(self):
        self.uuid = uuid.uuid4()

    def update(self, temperature: float, humidity: float, pressure: float):
        raise NotImplementedError


class Subject:
    """The only thing that the subject knows about an observer is that it implements a certain interface.
    It does not need to know about the concrete class of the observer (see below), what it does, or anything.

    Changes to either the subject or an observer will not affect the other. Because the two are loosely coupled,
    we are free to make changes to either, as long as the objects still meet their obligations to implement the subject
    or observer interfaces.
    """

    def register_observer(self, observer: Observer):
        raise NotImplementedError

    def remove_observer(self, observer: Observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class Display:

    @classmethod
    def display(cls):
        raise NotImplementedError


class GenericDisplay(Observer, Display):

    def __init__(self, weather_data: Subject):
        super().__init__()
        self.weather_data = weather_data
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

        weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        print("The values have been updated.")
        self.display()

    def display(self) -> None:
        print(f"The values for temperature, humidity and pressure are now, respectively "
              f"{self.temperature} , {self.humidity}, {self.pressure}.")


class WeatherData(Subject):

    def __init__(self):
        # having chosen a concrete data type to store the observers, one can now implement the remaining methods.
        self.observers: dict = {}
        self.temperature: float = 0.0
        self.humidity: float = 0.0
        self.pressure: float = 0.0

    def register_observer(self, observer: Observer) -> None:
        self.observers[observer.uuid] = observer

    def remove_observer(self, observer: Observer) -> None:
        if observer.uuid in self.observers.keys():
            self.observers.pop(observer.uuid)

    def notify_observers(self) -> None:
        for observer in self.observers.values():
            observer.update(temperature=self.temperature, humidity=self.humidity, pressure=self.pressure)
        print("Observers have been notified.")

    def measurements_changed(self) -> None:
        print("Measurements have changed.")
        self.notify_observers()

    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        print("New measurements have been set.")
        self.measurements_changed()


class WeatherStation:
    def __init__(self):
        self.weather_data = WeatherData()

    def generate_measurements(self):
        GenericDisplay(weather_data=self.weather_data)

        for i in range(1, 5):
            temperature = random.uniform(10, 20)
            humidity = random.uniform(50, 100)
            pressure = random.uniform(1.1, 1.5)
            self.weather_data.set_measurements(temperature=temperature, humidity=humidity, pressure=pressure)
            print(self.weather_data.observers)
            sleep(1)


if __name__ == '__main__':
    montana_weather_data = WeatherData()

    montana_obs = None

    # add two observers
    for _ in range(1, 3):
        montana_obs = GenericDisplay(weather_data=montana_weather_data)

    print(montana_weather_data.observers)
    assert montana_obs is not None

    montana_weather_data.remove_observer(observer=montana_obs)  # remove the last added observer
    print(montana_weather_data.observers)

    # initial weather values
    montana_weather_data.set_measurements(temperature=15.0, humidity=85.3, pressure=1.1)
    # note that, after set_measurements, the observers have already been notified
    assert ([observer.temperature for observer in montana_weather_data.observers.values()] ==
            [15.0] * len(montana_weather_data.observers))

    weather_station = WeatherStation()
    weather_station.generate_measurements()
