from app.hospital import Hospital


class Communicator:
    """Controller and Presentator"""

    def __init__(self):
        self.hospital = Hospital()
        self._commands_dict = {
            "узнать статус пациента": "get status",
            "повысить статус пациента": "status up",
            "понизить статус пациента": "status down",
            "выписать пациента": "discharge",
            "рассчитать статистику": "calculate statistics",
            "стоп": "stop"
        }

    def get_command(self) -> str | None:
        command_input = input("Введите команду: ").lower()
        for key, value in self._commands_dict.items():
            if command_input == key or command_input == value:
                return key
        self.notify_unknown_command()

    def get_id(self) -> int | None:
        id_input = input("Введите ID: ")
        if not id_input.isdigit() or int(id_input) < 0:
            self.notify_id_invalid_error()
        elif int(id_input) not in range(201) or self.hospital.is_patient_discharged(int(id_input) - 1):
            self.notify_id_off_range_error()
        else:
            return int(id_input)

    def print_patient_status(self, status: str):
        print(f'Статус пациента: "{status}"')

    def print_new_patient_status(self, status: str):
        print(f'Новый статус пациента: "{status}"')

    def is_patient_ready_for_discharge(self) -> bool:
        request = input("Желаете выписать этого клиента? (да/нет): ")
        return bool(request.lower() == "да")

    def notify_status_unchanged(self):
        print('Пациент остался в статусе "Готов к выписке"')

    def notify_cannot_downgrade_status_error(self):
        print("Ошибка. Нельзя понизить самый низкий статус (наши пациенты не умирают)")

    def notify_patient_is_discharged(self):
        print("Пациент выписан из больницы")

    def notify_id_invalid_error(self):
        print("Ошибка. ID пациента должно быть числом (целым, положительным)")

    def notify_id_off_range_error(self):
        print("Ошибка. В больнице нет пациента с таким ID")

    def notify_unknown_command(self):
        print(f'Неизвестная команда! Попробуйте ещё раз')

    def notify_session_end(self):
        print("Сеанс завершён.")

    def print_statistics(self, stat):
        print(stat)

