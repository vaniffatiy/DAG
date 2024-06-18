from conftest import validate_id
from app.data import commands


class RunCommands:
    def __init__(self, app):
        self.app = app
        self.commands = self.app.commands

    @validate_id
    def process_command(self, input_command: str, id: int = None):
        command = input_command.lower()
        if command in commands["узнать"]:
            self.commands.get_status_by_id(id)
        elif command in commands["повысить"]:
            self.commands.upgrade_status(id)
        elif command in commands["понизить"]:
            self.commands.downgrade_status(id)
        elif command in commands["выписать"]:
            self.commands.discharge_patient(id)
        elif command in commands["рассчитать"]:
            self.commands.calculate_statistics()
        elif command in commands["стоп"]:
            exit()
        else:
            print(f"Неизвестная команда: {command}! Попробуйте ещё раз")

