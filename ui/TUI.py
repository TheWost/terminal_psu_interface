import os
from colorama import Fore, Style, init
import warnings
from core.exceptions import InvalidDriverError


warnings.filterwarnings("ignore", category=UserWarning, module="pyvisa") # Removes warnings from querying output
init(autoreset=True) # Colorama auto-reset after each print

class Tui:
    def __init__(self, drivers):

        self.__drivers = drivers
        self.__driver = self.__chose_driver()

        if not hasattr(self.__driver, "get_actions"):
            raise InvalidDriverError("Driver must have method called .get_actions()")


        if hasattr(self.__driver, "mark") and hasattr(self.__driver, "name"):
            self.mark, self.name = self.__driver.mark, self.__driver.name

        else:

            if hasattr(self.__driver, "identify"):
                self.mark, self.name = self.__driver.identify()
            else:
                self.mark, self.name = "Not", "Found"

        self.__actions = self.__driver.get_actions()


    def __chose_driver(self):
        for i, driver in enumerate(self.__drivers, start=1):
            print(f"{i}. {driver}")

        choice = self.__int_input(len(self.__drivers))
        return self.__drivers[choice - 1]()


    def clear(self):
        os.system("cls" if os.name == 'nt' else 'clear')


    def __invalid_input_text(self):
        return f"{Fore.RED}{Style.BRIGHT}Invalid input."

    def __print_menu(self):
        header = f" === {self.mark} {self.name} ==="
        print(header)


        for index, desc in enumerate(self.__actoins.keys()):
            print(index + "." + desc)
        print((index + 1) + "." + "EXIT")

    def __int_input(self, choices_count):
        while True:
            try:
                user_choice = int(input("> "))

                if 1 <= user_choice <= choices_count:
                    return user_choice

                self.__invalid_input_text()


            except ValueError:
                input(self.__invalid_input_text("Input must be an integer!"))

            except KeyboardInterrupt:
                exit()

    def get_user_choice(self):
        return self.__int_input(len(self.__actions))


    def get_action_by_index(self,user_choice):
        if not user_choice:
            return
        return list(self.__actions.value())[user_choice] # If something here breaks. Please change from items to keys. And then using that key get action.

    def run(self):
        while True:
            self.clear()
            self._print_menu()
            user_choice = self.get_user_choice()
            action = self.get_action_by_index(user_choice)
            self.clear()
            action()
