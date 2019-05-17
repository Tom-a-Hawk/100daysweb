import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse


# helper function to load data
def _load_animal_data():
    with open("animal_data.json") as fin:
        animals = json.loads(fin.read())
        return {animal["id"]: animal for animal in animals}


animals = _load_animal_data()

VALID_ANIMALS = set([animal["animal"] for animal in animals.values()])

ANIMAL_NOT_FOUND = 'Animal not found'
# definition


class Animal(types.Type):
    id = validators.Integer(allow_null=True)
    animal = validators.String(enum=list(VALID_ANIMALS))
    scientific_name = validators.String(max_length=200)
    age = validators.Integer(minimum=0, maximum=2050)
    name = validators.String(max_length=250)

# API Methods

def list_animals() -> List[Animal]:
    return [Animal(animal[1]) for animal in sorted(animals.items())]


def create_animal(animal: Animal) -> JSONResponse:
    animal_id = len(animals) + 1
    animal.id = animal_id
    animals[animal_id] = animal
    return JSONResponse(Animal(animal), status_code=201)


def get_animal(animal_id: int) -> JSONResponse:
    animal = animals.get(animal_id)
    if not animal:
        error = {'error': ANIMAL_NOT_FOUND}
        return JSONResponse(error, status_code=404)

    return JSONResponse(Animal(animal), status_code=200)


def update_animal(animal_id: int, animal: Animal) -> JSONResponse:
    if not animals.get(animal_id):
        error = {'error': ANIMAL_NOT_FOUND}
        return JSONResponse(error, status_code=404)

    animal.id = animal_id
    animals[animal_id] = animal
    return JSONResponse(Animal(animal), status_code=200)


def delete_animal(animal_id: int) -> JSONResponse:
    if not animals.get(animal_id):
        error = {'error': ANIMAL_NOT_FOUND}
        return JSONResponse(error, status_code=404)

    del animals[animal_id]
    return JSONResponse({}, status_code=204)


routes = [
    Route('/', method='GET', handler=list_animals),
    Route('/', method='POST', handler=create_animal),
    Route('/{animal_id}/', method='GET', handler=get_animal),
    Route('/{animal_id}/', method='PUT', handler=update_animal),
    Route('/{animal_id}/', method='DELETE', handler=delete_animal),
]

app = App(routes=routes)


if __name__ == '__main__':
    app.serve('127.0.0.1', 5000, debug=True)