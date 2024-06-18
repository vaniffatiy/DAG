# from enum import Enum

# from conftest import *

# statuses = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

# commands = {
#     "узнать статус пациента": "get status",
#     "повысить статус пациента": "status up",
#     "понизить статус пациента": "status down",
#     "выписать пациента": "discharge",
#     "рассчитать статистику": "calculate statistics",
#     "стоп": "stop"
# }

# patients_list = []
# for _ in range(200):
#     patients_list.append(1)


# def filter_invalid_values(id: int):
#     response = ""
#     if type(id) is not int or id < 0:
#         response = "ID пациента должно быть числом (целым, положительным)"
#         print(response)
#     elif id not in range(201):
#         response = "В больнице нет пациента с таким ID"
#         print(response)
#     else:
#         response = None
#
#     return response

# class Status(Enum):
#     CHECK = Enum("узнать статус пациента", "get status")
#     RAISE = Enum("повысить статус пациента", "status up")
#     LOWER = Enum("понизить статус пациента", "status down")


# def get_status_by_id(id: int):
#     status_index = patients_list[id-1]
#     if status_index is None:
#         print("Этот пациент выписан")
#     else:
#         print(statuses[status_index])
#
#
# def upgrade_status(id: int):
#     index = id-1
#     if patients_list[index] < 3:
#         patients_list[index] += 1
#         print(f"Новый статус пациента: {statuses[patients_list[index]]}")
#     else:
#         request = input("Желаете выписать этого клиента? (да/нет): ")
#         if request.lower() == "да":
#             discharge_patient(id)
#         else:
#             print("Статус пациента не изменился")
#
#
# def downgrade_status(id: int):
#     index = id-1
#     if patients_list[index] > 0:
#         patients_list[index] -= 1
#         print(f"Новый статус пациента: {statuses[patients_list[index]]}")
#     else:
#         # raise ValueError("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
#         print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")
#
#
# def discharge_patient(id: int):
#     patients_list[id-1] = None
#     print("Пациент выписан из больницы")
#
#
# def filter_patients_list(status: int):
#     filtered_list = []
#     for patient in patients_list:
#         if status == 0 and patient == 0:
#             filtered_list.append(patient)
#         if status == 1 and patient == 1:
#             filtered_list.append(patient)
#         if status == 2 and patient == 2:
#             filtered_list.append(patient)
#         if status == 3 and patient == 3:
#             filtered_list.append(patient)
#     return filtered_list
#
#
# # @property
# def calculate_statistics():
#     patients = [patient for patient in patients_list if patient is not None]
#     stat = f'В больнице на данный момент находится {len(patients)} чел., из них: \n'
#     for i in range(4):
#         if len(filter_patients_list(i)) > 0:
#             stat += f'в статусе {statuses[i]}: {len(filter_patients_list(i))} чел. \n'
#     print(stat)


# def process_command(input_command: str, id:int = None):
#     if id is not None:
#         while filter_invalid_values(id) is not None:
#             response = input("Введите правильный ID:")
#             id = int(response)
#     command = input_command.lower()
#     if command in commands:
#         action = commands[command]
#         if action in commands["узнать"]:
#             get_status_by_id(id)
#         if action in commands["повысить"]:
#             upgrade_status(id)
#         if action in commands["понизить"]:
#             downgrade_status(id)
#         if action in  commands["выписать"]:
#             discharge_patient(id)
#         if action in commands["рассчитать"]:
#             calculate_statistics()
#         if action in commands["стоп"]:
#             exit()
#     else:
#         print(f"Неизвестная команда: {command}! Попробуйте ещё раз")
#
#
# process_command("повысить статус пациента", 3)
# process_command("get status", 5)
# process_command("повысить статус пациента", 3)
# process_command("повысить статус пациента", 3)
# process_command("узнать статус пациента", 4)
# process_command("понизить статус пациента", 4)
# process_command("понизить статус пациента", 4)
# process_command("выписать пациента", 5)
# process_command("рассчитать статистику")
# process_command("стоп")



