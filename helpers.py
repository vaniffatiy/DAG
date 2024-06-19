import pytest

from app.application import Application
from app.data import patients_list


def filter_invalid_values(id: int) -> str:
    response = ""
    if type(id) is not int or id < 0:
        response = "ID пациента должно быть числом (целым, положительным)"
        print(response)
    elif id not in range(201):
        response = "В больнице нет пациента с таким ID"
        print(response)
    else:
        response = None

    return response


def validate_id(func):
    def wrapper(*args,  **kwargs):
        if 'id' in kwargs:
            id = kwargs['id']
        else:
            return func(*args, **kwargs)
        if id is not None and filter_invalid_values(id) is not None:
            while True:
                response = input("Введите правильный ID:")
                id = int(response)
                if filter_invalid_values(id) is None:
                    break
            kwargs['id'] = id
        return func(*args, **kwargs)
    return wrapper


def filter_patients_list(status: int) -> list:
    filtered_list = []
    for patient in patients_list:
        if status == 0 and patient == 0:
            filtered_list.append(patient)
        if status == 1 and patient == 1:
            filtered_list.append(patient)
        if status == 2 and patient == 2:
            filtered_list.append(patient)
        if status == 3 and patient == 3:
            filtered_list.append(patient)
    return filtered_list


@pytest.fixture
def app() -> Application:
    return Application()
