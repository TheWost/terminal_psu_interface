from pathlib import Path
from ..connect import PsuConnection

class Instrument:
    def __init__(self):
        self.__inst = PsuConnection.connect()
        self.mark, self.name = _prase_name()

    def _parse_name(self):
        unprased_name = self.__inst.query("*IDN?")
        match = re.search(r"^([^,]+),([^,]+)", unprased_name)

        if match:
            return match.group(1).strip(), match.group(2).strip()
        return "Name", "not found"

    def identify(self):
        return self.__inst.query("*IDN?")

    def set_frequency(self):
        self.clear()
        current_frequency = self.__inst.query("FREQ?")
        current_frequency_prased = self._prase_the_number(current_frequency)
        print(Fore.YELLOW + Style.BRIGHT + f"Current frequency {current_frequency_prased:g}")
        freq = input(Fore.YELLOW + "Frequency [Hz]: ")
        self.__inst.write(f"FREQ {freq}")

     def set_voltage(self):
        self.clear()
        current_voltage = self.__inst.query("VOLT?")
        current_voltage_prased = self._prase_the_number(current_voltage)
        print(Fore.YELLOW + Style.BRIGHT + f"Current Voltage: {current_voltage_prased:g}")
        voltage = input(Fore.YELLOW + "Voltage [V]: ")
        self.__inst.write(f"VOLT {voltage}")

    def set_sin(self):
        self.__inst.write("FUNC SIN")

    def set_sqr(self):
        self.__inst.write("FUNC SQUARE")

    def set_ramp(self):
        self.__inst.write("FUNC RAMP")

    def set_pulse(self):
        self.__inst.write("FUNC PULSE")

    def set_noise(self):
        self.__inst.write("FUNC NOISE")

    def set_output_off(self):
        self.__inst.write("OUTP OFF")

    def set_output_on(self):
        self.__inst.write("OUTP ON")





#
#    def set_waveform(self):
#        while True:
#            self.clear()
#            self._print_waveforms()
#            choice = input("> ")
#
#            match choice:
#                case "1":
#                    self.inst.write("FUNC SIN")
#                    break
#                case "2":
#                    self.inst.write("FUNC SQUARE")
#                    break
#                case "3":
#                    self.inst.write("FUNC RAMP")
#                    break
#                case "4":
#                    self.inst.write("FUNC PULSE")
#                    break
#                case "5":
#                    self.inst.write("FUNC NOISE")
#                    break
#                case "6":
#                    break
#                case _:
#                    input(Fore.RED + Style.BRIGHT + "Invalid option.")
