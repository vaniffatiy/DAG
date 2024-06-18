from conftest import filter_patients_list
from data import patients_list, statuses


class Commands:
    def __init__(self):
        pass
    """на сегодня создание класса кажется излишним"""

    def get_status_by_id(self, id: int):
        status_index = patients_list[id-1]
        if status_index is None:
            print("Этот пациент выписан")
        else:
            print(statuses[status_index])

    def upgrade_status(self, id: int):
        index = id-1
        if patients_list[index] < 3:
            patients_list[index] += 1
            print(f"Новый статус пациента: {statuses[patients_list[index]]}")
        else:
            request = input("Желаете выписать этого клиента? (да/нет): ")
            if request.lower() == "да":
                self.discharge_patient(id)
            else:
                print("Статус пациента не изменился")

    def downgrade_status(self, id: int):
        index = id-1
        if patients_list[index] > 0:
            patients_list[index] -= 1
            print(f"Новый статус пациента: {statuses[patients_list[index]]}")
        else:
            # raise ValueError("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
            print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")

    def discharge_patient(self, id: int):
        patients_list[id-1] = None
        print("Пациент выписан из больницы")

    def calculate_statistics(self):
        patients = [patient for patient in patients_list if patient is not None]
        stat = f'В больнице на данный момент находится {len(patients)} чел., из них: \n'
        for i in range(4):
            if len(filter_patients_list(i)) > 0:
                stat += f'в статусе {statuses[i]}: {len(filter_patients_list(i))} чел. \n'
        print(stat)
