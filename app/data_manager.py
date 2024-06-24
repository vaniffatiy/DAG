patients_list = [1 for _ in range(200)]
statuses_dict = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}
commands_dict = {
    "узнать статус пациента": "get status",
    "повысить статус пациента": "status up",
    "понизить статус пациента": "status down",
    "выписать пациента": "discharge",
    "рассчитать статистику": "calculate statistics",
    "стоп": "stop"
}


class DataManager:

    def __init__(self):
        self.patients_list = patients_list
        self._statuses_dict = statuses_dict
        self._commands_dict = commands_dict

    def verify_command_type(self, command: str, request: str) -> bool:
        found = False
        for k, v in self._commands_dict.items():
            if command in (k, v):
                if request == "any_valid":
                    found = True
                elif request in (k, v):
                    found = True
        return found

    def get_status_name(self, index) -> str:
        return self._statuses_dict[index]

    def get_status(self, index) -> int | None:
        return self.patients_list[index] if index in range(201) else None
