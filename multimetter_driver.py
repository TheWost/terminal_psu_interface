from pathlib import Path
from core.connect import PsuConnection
from my_drivers.instrument import Instrument


class MultiMetter(Instrument):
    def __init__(self):
        super().__init__(PsuConnection.connect())

    def set_voltage(self):
        self._set_input("VOLT", "Voltage", "V")

    def set_current(self):
        self._set_input("CURR", "Current", "C")

    def set_output_off(self):
        self._inst.write("OUTP OFF")

    def set_output_on(self):
        self._inst.write("OUTP ON")


