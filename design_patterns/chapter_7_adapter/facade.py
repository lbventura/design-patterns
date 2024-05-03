# The Facade pattern provides a unified interface to a set of interfaces in a subsystem.
# Facades define a higher-level interface that makes the subsystem easier to use.

class Amplifier:

    @classmethod
    def on(cls):
        pass

    @classmethod
    def off(cls):
        pass


class PopcornPopper:

    @classmethod
    def on(cls):
        pass

    @classmethod
    def off(cls):
        pass


class TheaterLights:

    @classmethod
    def on(cls):
        pass

    @classmethod
    def off(cls):
        pass

    @classmethod
    def dim(cls):
        pass


class Projector:
    @classmethod
    def on(cls):
        pass

    @classmethod
    def off(cls):
        pass

    @classmethod
    def set_wide_screen_mode(cls):
        pass


class DVDPlayer:

    @classmethod
    def on(cls):
        pass

    @classmethod
    def off(cls):
        pass


class HomeTheaterFacade:
    """Because we do not want the user of the HomeTheater to have to do all the individual operations
    itself, we wrap these in the `prepare_movie` method."""

    def __init__(self, amplifier: Amplifier, popper: PopcornPopper,
                 theater_lights: TheaterLights, projector: Projector, dvd_player: DVDPlayer):
        self.amplifier = amplifier
        self.popper = popper
        self.theater_lights = theater_lights
        self.projector = projector
        self.dvd_player = dvd_player

    def prepare_movie(self):
        print("Preparing everything to watch a movie")
        self.popper.on()
        self.theater_lights.dim()
        self.projector.on()
        self.dvd_player.on()
        self.popper.off()
        print("All set!")


class MovieWatcher:
    # Client class of the HomeTheaterFacade
    def __init__(self, home_theater_facade: HomeTheaterFacade):
        self.home_theater_facade = home_theater_facade

    def enjoy_movie(self) -> None:
        self.home_theater_facade.prepare_movie()
        print("This movie is so good!")

    def dislike_movie(self) -> None:
        self.home_theater_facade.prepare_movie()
        print("This movie is absolute garbage!")


if __name__ == '__main__':
    amp = Amplifier()
    popp = PopcornPopper()
    lights = TheaterLights()
    proj = Projector()
    dvd_play = DVDPlayer()

    hmf = HomeTheaterFacade(amplifier=amp, popper=popp, theater_lights=lights, projector=proj, dvd_player=dvd_play)
    hmf.prepare_movie()

    mw = MovieWatcher(home_theater_facade=hmf)
    mw.enjoy_movie()
