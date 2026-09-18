from core.connect import PsuConnection
from my_drivers.instrument import Instrument


class MultiMetter(Instrument):
    def __init__(self):
        super().__init__(PsuConnection.connect())

    def set_voltage(self, value):
        self._inst.write(f"VOLT {value}")

    def set_current(self, value):
        self._inst.write(f"CURR {value}")

    def set_output_off(self):
        self._inst.write("OUTP OFF")

    def set_output_on(self):
        self._inst.write("OUTP ON")

    def get_actions(self):
        return {
            "set_voltage": {
                "func": self.set_voltage,
                "args": ["Voltage [V]"]
            },
            "set_current": {
                "func": self.set_current,
                "args": ["Current [CURR]"]
            },
            "set_output_on": {
                "func": self.set_output_on,
                "args": []
            },
            "set_output_off": {
                "func": self.set_output_off,
                "args": []
            }
        }