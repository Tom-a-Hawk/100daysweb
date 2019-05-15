import json
from typing import List

from apistar import App, Route, types, validators
from apistar.http import JSONResponse

from pprint import pprint



def _load_cars_data():
    with open('MOCK_DATA.json') as f:
        cars = json.loads(f.read())
        return {car["id"]: car for car in cars}


cars = _load_cars_data()
#pprint(cars)
#print(sorted(cars.items()))

VALID_MANUFACTURERS = set(car['manufacturer'] for car in cars.values())
#pprint(VALID_MANUFACTURERS)
#print(type(VALID_MANUFACTURERS))

CAR_NOT_FOUND = 'Car not found'


# definition


class Car(types.Type):
    id = validators.Integer(allow_null=True)  # assign in POST
    manufacturer = validators.String(enum=list(VALID_MANUFACTURERS))
    model = validators.String(max_length=50)
    year = validators.Integer(minimum=1900, maximum=2050)
    vin = validators.String(max_length=50, default='')