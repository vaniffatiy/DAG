from app.hospital import Hospital


class Communicator:
    """Controller and Presentator"""

    def __init__(self):
        self.hospital = Hospital()

    def get_command(self) -> str | None:
        command_input = input("Введите команду: ").lower()
        if self.hospital.verify_command_type(command_input, "any_valid"):
            return command_input
        else:
            self.notify_unknown_command()
            return None

    def get_id(self) -> int | None:
        id_input = input("Введите ID: ")
        response = self.hospital.filter_id_values(id_input)
        if response == "invalid":
            self.notify_id_invalid_error()
        if response == "off_range":
            self.notify_id_off_range_error()
        if response == "OK":
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

