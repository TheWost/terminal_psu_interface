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

        self.mark = self.__driver.mark
        self.name = self.__driver.name
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

    def _print_menu(self):
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
        user_key = list(self.__actions)[user_choice]
        action = self.__actions[user_key]
        return action

    def _handle_action(self, action):
        if not action["args"]:
            action["func"]()
            return

        args = []
        self.clear()
        for arg in action["args"]:
            print(arg)
            args.append(input("> "))

        action["func"](*args)
        input("Press Enter to continue...")
        
    def run(self):
        while True:
            self.clear()
            self._print_menu()
            user_choice = self.get_user_choice()
            action = self.get_action_by_index(user_choice)
            self._handle_action(action)