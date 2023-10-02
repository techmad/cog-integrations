import yaml
from pathlib import Path

def yaml2dict():
    p = Path(__file__).with_name('config.yml')
    with p.open('r') as file:
        return yaml.safe_load(file.read())