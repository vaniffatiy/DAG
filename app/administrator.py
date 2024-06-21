from app.commands import Commands


commands = Commands()
hospital = commands.hospital
communicator = commands.communicator


def receive_and_process_command():
    session_active = True
    while session_active:
        command_input = communicator.get_command()
        if hospital.verify_command_type(command_input, "stop"):
            session_active = False
            communicator.notify_session_end()
            return
        if hospital.verify_command_type(command_input, "any_valid"):
            process_command(command_input)
        else:
            communicator.notify_unknown_command()


def process_command(command: str):
    if hospital.verify_command_type(command, "calculate"):
        commands.calculate_statistics()
        return
    elif hospital.verify_command_type(command, "stop"):
        return
    id = ask_and_validate_id()
    if id is not None:
        index = id - 1
        if hospital.verify_command_type(command, "check"):
            commands.get_status_by_id(index)
        elif hospital.verify_command_type(command, "upgrade"):
            commands.upgrade_status(index)
        elif hospital.verify_command_type(command, "downgrade"):
            commands.downgrade_status(index)
        elif hospital.verify_command_type(command, "discharge"):
            commands.discharge_patient(index)


def ask_and_validate_id() -> int | None:
    id_input = communicator.get_id()
    if is_id_valid(id_input):
        return int(id_input)
    else:
        return None


def is_id_valid(index: str) -> bool:
    response = hospital.filter_id_values(index)
    if response == "invalid":
        communicator.notify_id_invalid_error()
    if response == "off_range":
        communicator.notify_id_off_range_error()
    if response == "OK":
        return True
