class Communicator:
    """Controller and Presentator"""

    def print_patient_status(self, status: str):
        print(f'Статус пациента: "{status}"')

    def print_new_patient_status(self, status: str):
        print(f'Новый статус пациента: "{status}"')

    def get_command(self) -> str:
        return input("Введите команду: ").lower()

    def get_id(self) -> str:
        return input("Введите ID: ")

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

