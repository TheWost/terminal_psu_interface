import re

class Instrument:
    def __init__(self, inst):
        self._inst = inst
        self.mark, self.name = self._parse_name()

    def _parse_the_number(self, number):
        return int(float(number))

    def _parse_name(self):
        raw_name = self._inst.query("*IDN?")
        match = re.search(r"^([^,]+),([^,]+)", raw_name)

        if match:
            return match.group(1).strip(), match.group(2).strip()

        return "Name", "not found"

    def identify(self):
        return self._inst.query("*IDN?")