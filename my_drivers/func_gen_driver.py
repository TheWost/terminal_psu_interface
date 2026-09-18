from pathlib import Path
from core.connect import PsuConnection
from my_drivers.instrument import Instrument

class FunctionGenerator(Instrument):
    def __init__(self):
        super().__init__(PsuConnection.connect())

    def set_frequency(self):
        self._set_input("FREQ","Frequency","Hz")

    def set_voltage(self):
        self._set_input("VOLT", "Voltage", "V")

    def set_sin(self):
        self._inst.write("FUNC SIN")

    def set_sqr(self):
        self._inst.write("FUNC SQUARE")

    def set_ramp(self):
        self._inst.write("FUNC RAMP")

    def set_pulse(self):
        self._inst.write("FUNC PULSE")

    def set_noise(self):
        self._inst.write("FUNC NOISE")

    def set_output_off(self):
        self._inst.write("OUTP OFF")

    def set_output_on(self):
        self._inst.write("OUTP ON")
