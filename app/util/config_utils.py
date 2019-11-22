import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent


def load_config(path):
    with open(path, 'r') as file:
        config = yaml.load(file)
    return config
