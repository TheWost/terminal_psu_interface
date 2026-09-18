from my_drivers.func_gen_driver import FunctionGenerator
from my_drivers.multimetter_driver import MultiMetter
from ui.TUI import Tui


def main():
    drivers = [FunctionGenerator, MultiMetter]
    Tui(drivers).run()





if __name__ == "__main__":
    main()
