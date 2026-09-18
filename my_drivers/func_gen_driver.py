from core.connect import PsuConnection
from my_drivers.instrument import Instrument

class FunctionGenerator(Instrument):
    def __init__(self):
        super().__init__(PsuConnection.connect())

    def set_frequency(self, value):
        self._inst.write(f"CURR {value}")

    def set_voltage(self, value):
        self._inst.write(f"VOLT {value}")

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

    def get_actions(self):
        return {
            "Identify": {
                "func": self.identify,
                "args": []
            },
            "Set frequency": {
                "func": self.set_frequency,
                "args": ["Frequency [Hz]"]
            },
            "Set voltage": {
                "func": self.set_voltage,
                "args": ["Voltage [V]"]
            },
            "Set sine": {
                "func": self.set_sin,
                "args": []
            },
            "Set square": {
                "func": self.set_sqr,
                "args": []
            },
            "Set ramp": {
                "func": self.set_ramp,
                "args": []
            },
            "Set pulse": {
                "func": self.set_pulse,
                "args": []
            },
            "Set noise": {
                "func": self.set_noise,
                "args": []
            },
            "Output on": {
                "func": self.set_output_on,
                "args": []
            },
            "Output off": {
                "func": self.set_output_off,
                "args": []
            }
        }