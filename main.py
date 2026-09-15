from my_drivers.func_gen_driver import FunctionGenerator
from ui.TUI import Tui


def main():
    drivers = [FunctionGenerator]
    Tui(drivers).run()





if __name__ == "__main__":
    main()
