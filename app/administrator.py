from app.commands import Commands


commands = Commands()
hospital = commands.hospital
communicator = commands.communicator


def run_session():
    session_active = True
    while session_active:
        command_input = communicator.get_command()
        if command_input is not None:
            if hospital.verify_command_type(command_input, "stop"):
                session_active = False
                communicator.notify_session_end()
                return
            process_command(command_input)


def process_command(command: str):
    if hospital.verify_command_type(command, "calculate statistics"):
        commands.calculate_statistics()
        return
    elif hospital.verify_command_type(command, "stop"):
        return
    id = communicator.get_id()
    if id is not None:
        index = id - 1
        if hospital.verify_command_type(command, "get status"):
            commands.get_status_by_id(index)
        elif hospital.verify_command_type(command, "status up"):
            commands.upgrade_status(index)
        elif hospital.verify_command_type(command, "status down"):
            commands.downgrade_status(index)
        elif hospital.verify_command_type(command, "discharge"):
            commands.discharge_patient(index)


