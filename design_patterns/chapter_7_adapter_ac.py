class USPlug:
    @classmethod
    def connect_to_us_power(cls) -> str:
        return "Now the US plug is connected to power."

    @classmethod
    def disconnect_from_us_power(cls) -> str:
        return "Now the US plug disconnected from power."


class GBPlug:

    @classmethod
    def connect_to_gb_power(cls) -> str:
        return "Now the GB plug is connected to power."

    @classmethod
    def disconnect_from_gb_power(cls) -> str:
        return "Now the GB plug disconnected from power."


class UStoGBAdaptor(GBPlug):
    # takes US plug and adapts it to GB
    def __init__(self, plug: USPlug):
        self.plug = plug

    def connect_to_gb_power(self) -> str:
        return self.plug.connect_to_us_power() + " " + "But it using an adaptor."

    def disconnect_from_gb_power(self) -> str:
        return self.plug.disconnect_from_us_power()


class PlayingGuitarInGB:
    def __init__(self, plug: GBPlug):
        self.plug = plug

    def turn_on_amplifier(self) -> str:
        print(self.plug.connect_to_gb_power())
        return "It is time for rock-and-roll like the Beatles!"


class UStoGBAdaptorExtra(GBPlug):

    def __init__(self, adapted_plug: UStoGBAdaptor):
        self.adapted_plug = adapted_plug

    def protect_from_lightning(self) -> str:
        print(self.adapted_plug.connect_to_gb_power())
        return "A lightening struck, but because this is protected, nothing bad happened!"


if __name__ == '__main__':
    us_cable = USPlug()
    gb_adapter = UStoGBAdaptor(plug=us_cable)

    playing_gb_guitar = PlayingGuitarInGB(plug=GBPlug())
    print(playing_gb_guitar.turn_on_amplifier())

    playing_us_guitar_in_gb = PlayingGuitarInGB(plug=gb_adapter)
    print(playing_us_guitar_in_gb.turn_on_amplifier())

    gb_adapter_extra = UStoGBAdaptorExtra(adapted_plug=gb_adapter)
    print(gb_adapter_extra.protect_from_lightning())
