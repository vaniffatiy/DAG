from helpers import is_id_valid
from app.data import commands_dict
from . import commands


def receive_and_process_command():
    session_active = True
    while session_active:
        command_input = input("Введите команду: ").lower()
        if command_input in commands_dict["стоп"]:
            session_active = False
            print("Сеанс завершён.")
            return
        found = False
        for c in commands_dict:
            if command_input in commands_dict[c]:
                found = True
                process_command(command_input)
                if command_input in commands_dict["стоп"]:
                    session_active = False
                    print("Сеанс завершён.")
                    break
        if not found:
            print(f'Неизвестная команда! Попробуйте ещё раз')


def process_command(command: str):
    if command in commands_dict["рассчитать"]:
        commands.calculate_statistics()
        return
    elif command in commands_dict["стоп"]:
        return
    id = add_id()
    if id is not None:
        if command in commands_dict["узнать"]:
            commands.get_status_by_id(id)
        elif command in commands_dict["повысить"]:
            commands.upgrade_status(id)
        elif command in commands_dict["понизить"]:
            commands.downgrade_status(id)
        elif command in commands_dict["выписать"]:
            commands.discharge_patient(id)


def add_id() -> int | None:
    id_input = input("Введите ID: ")
    if is_id_valid(id_input):
        return int(id_input)
    else:
        return None
