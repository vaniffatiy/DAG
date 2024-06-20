from app.data import patients_list


def filter_invalid_values(id: str) -> str:
    if not id.isdigit() or int(id) < 0:
        response = "Ошибка. ID пациента должно быть числом (целым, положительным)"
        print(response)
    elif int(id) not in range(201) or patients_list[int(id)-1] is None:
        response = "Ошибка. В больнице нет пациента с таким ID"
        print(response)
    else:
        response = None
    return response


def is_id_valid(id: str) -> bool:
    return filter_invalid_values(id) is None


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

