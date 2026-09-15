from connect import PsuConnection
import os
from colorama import Fore, Style, init
import warnings
import re
from exceptions import InvalidDriverError


warnings.filterwarnings("ignore", category=UserWarning, module="pyvisa") # Removes warnings from querying output
init(autoreset=True) # Colorama auto-reset after each print

class TUI:
    def __init__(self, driver):

        self.__driver = driver

        if not hasattr(self.__driver, "get_actions"):
            raise InvalidDriverError("Driver must have method called .get_actions()")

        if hasattr(self.__driver, "identify"):
            self.mark, self.name = self.__driver.identify()
        else:
            self.mark, self.name = "Not", "Found"

        self.__actions = self.__driver.get_actions()

    def clear(self):
        os.system("cls" if os.name == 'nt' else 'clear')

    def _print_menu(self):


        header = f" === {self.mark} {self.name} ==="
        print(header)


        for index, desc, action enumerate(self.__actoins):
            print(index + "." + desc)

    def _get_user_aciton(self, lenght = len(self.__actions)):
        if not lenght:
            return

        while True:
            try:
                user_choice = int(input("> "))





if __name__ == "__main__":
    TUI().run()

