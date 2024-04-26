from typing import List


class Command:

    def execute(self):
        raise NotImplementedError


class NoCommand(Command):

    def execute(self) -> None:
        print("Let me do nothing")
        pass


class Light:

    def __str__(self) -> str:
        return "Light"

    def on(self):
        pass

    def off(self):
        pass


class Stereo:

    def __str__(self) -> str:
        return "Stereo"

    def on(self):
        pass

    def off(self):
        pass

    def set_cd(self):
        pass

    def set_dvd(self):
        pass

    def set_radio(self):
        pass

    def set_volume(self, volume: int):
        pass


class GarageDoor:

    def __str__(self) -> str:
        return "Garage Door"

    def up(self):
        pass

    def down(self):
        pass

    def stop(self):
        pass


class Jacuzzi:

    def __str__(self) -> str:
        return "Jacuzzi"

    def on(self):
        pass

    def off(self):
        pass


class LightOnCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()
        print("Light was turned on")


class LightOffCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.off()
        print("Light was turned off")


class GarageDoorOpenCommand(Command):

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()
        print("The garage door is up")


class GarageDoorCloseCommand(Command):

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.down()
        print("The garage door is down")


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(volume=11)
        print("The stereo is now on, playing some Barry White")


class StereoOffCommand(Command):

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()
        print("The stereo is now off")


class JacuzziOnCommand(Command):

    def __init__(self, jacuzzi: Jacuzzi):
        self.jacuzzi = jacuzzi

    def execute(self) -> None:
        self.jacuzzi.on()
        print("BUBBLES! And it is soo warm...")


class JacuzziOffCommand(Command):

    def __init__(self, jacuzzi: Jacuzzi):
        self.jacuzzi = jacuzzi

    def execute(self) -> None:
        self.jacuzzi.off()
        print("Funtime is over.")


class MacroCommand(Command):

    def __init__(self, commands: List[Command]):
        self.commands = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()


class RemoteControl:

    def __init__(self):
        self.on_commands: List[Command] = [NoCommand() for _ in range(7)]
        self.off_commands: List[Command] = [NoCommand() for _ in range(7)]
        self.undo_command: Command = NoCommand()

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def press_on_button(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def press_off_button(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def press_undo_button(self) -> None:
        self.undo_command.execute()


class RemoteLoader:

    def __init__(self):
        self.remote_control: RemoteControl = RemoteControl()

    def set_garage_door_command(self, slot: int) -> None:
        outhouse_garage_door = GarageDoor()
        self.remote_control.set_command(slot=slot, on_command=GarageDoorOpenCommand(garage_door=outhouse_garage_door),
                                        off_command=GarageDoorCloseCommand(garage_door=outhouse_garage_door))

    def set_living_room_light(self, slot: int) -> None:
        living_room_light = Light()
        self.remote_control.set_command(slot=slot, on_command=LightOnCommand(light=living_room_light),
                                        off_command=LightOffCommand(light=living_room_light))

    def set_living_room_stereo(self, slot: int) -> None:
        living_room_stereo = Stereo()
        self.remote_control.set_command(slot=slot, on_command=StereoOnWithCDCommand(stereo=living_room_stereo),
                                        off_command=StereoOffCommand(stereo=living_room_stereo))

    def set_macro_command(self, slot: int) -> None:
        jacuzzi = Jacuzzi()
        living_room_stereo = Stereo()
        party_on_commands = MacroCommand(commands=[JacuzziOnCommand(jacuzzi=jacuzzi),
                                                   StereoOnWithCDCommand(stereo=living_room_stereo)])
        party_off_commands = MacroCommand(commands=[JacuzziOffCommand(jacuzzi=jacuzzi),
                                                    StereoOffCommand(stereo=living_room_stereo)])
        self.remote_control.set_command(slot=slot, on_command=party_on_commands, off_command=party_off_commands)

    def set_all_commands(self) -> None:
        all_commands = [self.set_garage_door_command, self.set_living_room_light, self.set_living_room_stereo,
                        self.set_macro_command]

        for slot, control in enumerate(self.remote_control.on_commands):
            if isinstance(control, NoCommand) and slot < len(all_commands):
                all_commands[slot](slot=slot)


if __name__ == '__main__':
    src = RemoteLoader()

    assert [isinstance(ele, NoCommand) for ele in src.remote_control.on_commands]
    src.set_all_commands()

    src.remote_control.press_on_button(slot=2)
    print("... Quitting just ain't my shtick ...")
    src.remote_control.press_undo_button()

    # Because no button was added to slot 2, pressing the on button should print
    # "Let me do nothing". If we had used the Command interface,
    # we would have raised a NonImplementedError
    src.remote_control.press_on_button(slot=6)

    src.remote_control.press_on_button(slot=3)
    print("... Never, never gonna give you up ...")
    src.remote_control.press_undo_button()
