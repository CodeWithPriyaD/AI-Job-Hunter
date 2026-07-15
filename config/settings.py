from pathlib import Path
import yaml

CONFIG_FILE = Path(__file__).parent / "config.yaml"

class Settings:
    def __init__(self):
        with open(CONFIG_FILE, "r") as file:
            self.config = yaml.safe_load(file)

    @property
    def app_name(self):
        return self.config["application"]["name"]

    @property
    def roles(self):
        return self.config["search"]["roles"]

    @property
    def locations(self):
        return self.config["search"]["locations"]

    @property
    def providers(self):
        return self.config["providers"]