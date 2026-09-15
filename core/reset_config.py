
import json
from pathlib import Path

data = {"psu" : ""}


config_path = Path(__file__).resolve().parent.parent / "config.json"

with open(config_path, "w") as f:
    json.dump(data, f)
