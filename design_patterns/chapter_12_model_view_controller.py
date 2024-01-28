from typing import List


class BeatObserver:

    @classmethod
    def update(cls):
        raise NotImplementedError


class BPMObserver:

    @classmethod
    def update_bpm(cls):
        raise NotImplementedError


class BeatModelInterface:

    @classmethod
    def initialize(cls):
        raise NotImplementedError

    @classmethod
    def on(cls):
        raise NotImplementedError

    @classmethod
    def off(cls):
        raise NotImplementedError

    @classmethod
    def set_bpm(cls, bpm: int):
        raise NotImplementedError

    @classmethod
    def get_bpm(cls) -> int:
        raise NotImplementedError

    @classmethod
    def register_observer(cls, beat_observer: BeatObserver):
        raise NotImplementedError

    @classmethod
    def remove_observer(cls, beat_observer: BeatObserver):
        raise NotImplementedError

    @classmethod
    def register_bpm_observer(cls, bpm_observer: BPMObserver):
        raise NotImplementedError

    @classmethod
    def remove_bpm_observer(cls, bpm_observer: BPMObserver):
        raise NotImplementedError


class MetaEventListener:

    @classmethod
    def set_up_midi(cls):
        pass

    @classmethod
    def build_track_and_start(cls):
        pass


class Sequencer:

    @classmethod
    def start(cls):
        pass

    @classmethod
    def stop(cls):
        pass

    @classmethod
    def set_tempo_in_bpm(cls, bpm: int):
        pass


class BeatModel(BeatModelInterface, MetaEventListener):

    def __init__(self, sequencer: Sequencer):
        self.sequencer = sequencer
        self.beat_observers: List[BeatObserver] = []
        self.bpm_observers: List[BPMObserver] = []
        self.bpm = 90

    def initialize(self) -> None:
        self.set_up_midi()
        self.build_track_and_start()

    def on(self) -> None:
        self.sequencer.start()
        self.set_bpm(90)

    def off(self) -> None:
        self.set_bpm(0)
        self.sequencer.stop()

    def set_bpm(self, bpm: int):
        self.bpm = bpm
        self.sequencer.set_tempo_in_bpm(self.bpm)
        self.notify_bpm_observers()

    def get_bpm(self) -> int:
        return self.bpm

    def notify_beat_observers(self) -> None:
        for beat_observer in self.beat_observers:
            beat_observer.update()

    def notify_bpm_observers(self) -> None:
        for bpm_observer in self.bpm_observers:
            bpm_observer.update_bpm()

    def register_observer(self, beat_observer: BeatObserver):
        self.beat_observers.append(beat_observer)

    def register_bpm_observer(self, bpm_observer: BPMObserver):
        self.bpm_observers.append(bpm_observer)


class ControllerInterface:

    @classmethod
    def start(cls):
        raise NotImplementedError

    @classmethod
    def stop(cls):
        raise NotImplementedError

    @classmethod
    def increase_bpm(cls):
        raise NotImplementedError

    @classmethod
    def decrease_bpm(cls):
        raise NotImplementedError

    @classmethod
    def set_bpm(cls, bpm: int):
        raise NotImplementedError


class BPMOutputLabel:

    def __init__(self):
        self.text: str = ""

    def set_text(self, text: str) -> None:
        self.text = text

    def print_text(self) -> None:
        print(self.text)


class DJView(BeatObserver, BPMObserver):

    def __init__(self, controller: ControllerInterface, model: BeatModelInterface, bpm_output_label: BPMOutputLabel):
        super().__init__()
        self.controller = controller
        self.model = model
        self.bpm_output_label = bpm_output_label
        model.register_observer(self)
        model.register_bpm_observer(self)

    def create_view(self):
        pass

    def create_controls(self):
        pass

    def update_bpm(self):
        bpm = self.model.get_bpm()

        if not bpm:
            self.bpm_output_label.set_text("Offline")
            self.bpm_output_label.print_text()
        else:
            self.bpm_output_label.set_text(f"Current BPM: {self.model.get_bpm()}")
            self.bpm_output_label.print_text()


class BeatController(ControllerInterface):

    def __init__(self, model: BeatModelInterface, bpm_output_label: BPMOutputLabel):
        self.model = model
        self.view = DJView(controller=self, model=model, bpm_output_label=bpm_output_label)
        self.view.create_view()
        self.view.create_controls()
        model.initialize()

    def start(self):
        self.model.on()

    def stop(self):
        self.model.off()

    def increase_bpm(self):
        bpm = self.model.get_bpm()
        self.model.set_bpm(bpm=bpm + 1)

    def decrease_bpm(self):
        bpm = self.model.get_bpm()
        self.model.set_bpm(bpm=bpm-1)

    def set_bpm(self, bpm: int):
        self.model.set_bpm(bpm=bpm)


if __name__ == '__main__':
    beat_model = BeatModel(sequencer=Sequencer())
    beat_controller = BeatController(model=beat_model, bpm_output_label=BPMOutputLabel())
    beat_controller.start()

    beat_controller.view.update_bpm()
    beat_controller.increase_bpm()

    beat_controller.stop()
    print(beat_model.get_bpm())
