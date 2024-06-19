from helpers import is_id_valid
from app.data import commands_dict
from . import commands


def receive_and_process_command():
    command_input = input("Введите команду:").lower()
    if command_input not in commands_dict["стоп"]:
        while True:
            found = False
            for c in commands_dict:
                if command_input in commands_dict[c]:
                    found = True
                    process_command(command_input)
                    if command_input in commands_dict["стоп"]:
                        print("Сеанс завершён.")
                        return
                    command_input = input("Введите команду:").lower()
            if not found:
                print(f'Неизвестная команда! Попробуйте ещё раз')
                command_input = input("Введите команду:").lower()
    else:
        print("Сеанс завершён.")


def process_command(command: str):
    if command in commands_dict["узнать"]:
        commands.get_status_by_id(add_id())
    elif command in commands_dict["повысить"]:
        commands.upgrade_status(add_id())
    elif command in commands_dict["понизить"]:
        commands.downgrade_status(add_id())
    elif command in commands_dict["выписать"]:
        commands.discharge_patient(add_id())
    elif command in commands_dict["рассчитать"]:
        commands.calculate_statistics()


def add_id() -> int:
    id_input = input("Введите ID:")
    if is_id_valid(id_input):
        return int(id_input)
    else:
        receive_and_process_command()




