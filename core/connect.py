import json
import pyvisa
from pathlib import Path



class PsuConnection:

    @staticmethod
    def load_config(config_path="config.json"):
        """Loads json config"""



        if Path(config_path).exists():
            with open(config_path, "r") as f:
                data = json.load(f)
                return data
        else:
            data = { "psu": "" }
            with open(config_path, "w") as f:
                json.dump(data, f)

            return data

    @staticmethod
    def save_config(psu_name, config_path="config.json"):
        """Saves json config"""
        data = PsuConnection.load_config(config_path)
        data["psu"] = psu_name 
        with open(config_path, "w") as f:
            json.dump(data, f)

    @staticmethod
    def choice(resources):
        """Prints out resources and lets user choose correct one"""
        if not resources:
            print("No psus found.")
            return None

        for number, resource in enumerate(resources, start=1):
            print(f"{number}. {resource}")

        choice = int(input("Choose psu: "))
        return resources[choice - 1]

    @staticmethod
    def connection_input(rm):
        """Returns available PSU devices that python can find"""
        resources = rm.list_resources()
        return PsuConnection.choice(resources)

    @staticmethod
    def connect():
        """Connects to choosen PSU and returns the instrument"""
        rm = pyvisa.ResourceManager(r"C:\Windows\System32\visa64.dll")

        psu_name = PsuConnection.load_config().get("psu")
        if not psu_name:
            psu_name = PsuConnection.connection_input(rm)

        if not psu_name:
            raise RuntimeError("No psu selected or available.")

        PsuConnection.save_config(psu_name)

        psu = rm.open_resource(psu_name)
        psu.read_termination = "\n"
        psu.write_termination = "\n"
        psu.send_end = True
        psu.query_delay = 0.1
        return psu




def main():
    print("First time setup")
    PsuConnection.connect()


if __name__ == "__main__":
    main()
