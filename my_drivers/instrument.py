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

    def _set_input(self, command, print_prompt, short_prompt=""):
        current = self._inst.query(f"{command}?")
        current_parsed = self._prase_the_number(current)

        print(Fore.YELLOW + Style.BRIGHT + f"Current {print_prompt}: {current_parsed:g}")

        value = input(Fore.YELLOW + f"{print_prompt} {f'[{short_prompt}]' if short_prompt else ''}: ")

        self._inst.write(f"{command} {value}")

    def identify(self):
        return self._inst.query("*IDN?")


    def get_actions(self):
        return dict(name for name, value in type(self).__dict__.items() if callable(value) and not name_startwith("_"))


