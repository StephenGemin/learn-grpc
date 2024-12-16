import json
from pathlib import Path


def read_recipe_db():
    with open(Path(__file__).parent / "random_recipes.json") as fio:
        return json.load(fio)
