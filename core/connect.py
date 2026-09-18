import json
import pyvisa
from pathlib import Path
from core.exceptions import ConnectionConfigurationProblem



class PsuConnection:
    CONFIG_PATH = Path(__file__).parent.parent / "config" / "config.json"

    @classmethod
    def connect(cls):
        with open(cls.CONFIG_PATH, "r") as f:
            config = json.load()

        resource_name = config["psu"]


        if not resource_name:
            raise ConnectionConfigurationProblem("Config dosen't have psu device configured")

        rm = pyvisa.ResourceManager()
        return rm.open_resource(resource_name)