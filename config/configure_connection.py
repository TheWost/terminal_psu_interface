import pyvisa
import json

class ConfigConnection:
    def __init__(self):
        self.config_path = "config.json"

    def get_user_choice(self, resources):
        """Prints out resources and lets user choose correct one"""
        if not resources:
            print("No devices found.")
            return None

        for number, resource in enumerate(resources, start=1):
            print(f"{number}. {resource}")

        choice = int(input("Choose device: "))
        return resources[choice - 1]

    def configure(self):
        """Gets device choosen by user and saves it."""
        
        rm = pyvisa.ResourceManager()
        resources = rm.list_resources()
        chosen_device = self.get_user_choice(resources)

        with open(self.config_path, "w") as f:
            if chosen_device:
                data = {"psu": chosen_device}
            else:
                data = {"psu": ""}
            json.dump(data,f)

def main():
    ConfigConnection().configure()


if __name__ == "__main__":
    main()
        