from helpers import filter_patients_list
from app.data import patients_list, statuses_dict


def get_status_by_id(id: int):
    status_index = patients_list[id-1]
    print(f'Статус пациента: "{statuses_dict[status_index]}"')


def upgrade_status(id: int):
    index = id-1
    if patients_list[index] < 3:
        patients_list[index] += 1
        print(f'Новый статус пациента: "{statuses_dict[patients_list[index]]}"')
    else:
        request = input("Желаете выписать этого клиента? (да/нет): ")
        if request.lower() == "да":
            discharge_patient(id)
        else:
            print('Пациент остался в статусе "Готов к выписке"')


def downgrade_status(id: int):
    index = id-1
    if patients_list[index] > 0:
        patients_list[index] -= 1
        print(f'Новый статус пациента: "{statuses_dict[patients_list[index]]}"')
    else:
        print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")


def discharge_patient(id: int):
    patients_list[id-1] = None
    print("Пациент выписан из больницы")


def calculate_statistics():
    patients = [patient for patient in patients_list if patient is not None]
    stat = f'В больнице на данный момент находится {len(patients)} чел., из них: \n'
    for i in range(4):
        if len(filter_patients_list(i)) > 0:
            stat += f'   - в статусе "{statuses_dict[i]}": {len(filter_patients_list(i))} чел. \n'
    print(stat)


