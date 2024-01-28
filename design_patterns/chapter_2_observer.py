import uuid
import random
from time import sleep


class Observer:

    def __init__(self):
        self.uuid = uuid.uuid4()

    def update(self, temperature: float, humidity: float, pressure: float):
        raise NotImplementedError


class Subject:

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
              f"{self.temperature} , {self.humidity}, {self.pressure}")


class WeatherData(Subject):

    def __init__(self):
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

    for _ in range(1, 3):
        montana_obs = GenericDisplay(weather_data=montana_weather_data)

    print(montana_weather_data.observers)
    montana_weather_data.remove_observer(observer=montana_obs)  # remove the last added observer

    print(montana_weather_data.observers)

    montana_weather_data.set_measurements(temperature=15.0, humidity=85.3, pressure=1.1)
    print(montana_weather_data.temperature)

    weather_station = WeatherStation()
    weather_station.generate_measurements()
