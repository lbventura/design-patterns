class Command:

    def execute(self):
        pass


class Light:

    def on(self):
        pass


class GarageDoor:

    def up(self):
        pass

    def down(self):
        pass

    def stop(self):
        pass


class LightOnCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()
        print("Light was turned on")


class GarageDoorOpenCommand(Command):

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()
        print("The garage door is up")


class SimpleRemoteControl:
    slot: Command = None

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


if __name__ == '__main__':
    src = SimpleRemoteControl()
    src.set_command(command=LightOnCommand(light=Light()))
    src.button_was_pressed()
    src.set_command(command=GarageDoorOpenCommand(garage_door=GarageDoor()))
    src.button_was_pressed()

