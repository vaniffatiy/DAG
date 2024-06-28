from app.commands import Commands


class Administrator:
    """Принимает и обрабатывает запрос, запускает нужные команды"""
    def __init__(self):
        self.commands = Commands()
        self.hospital = self.commands.hospital
        self.communicator = self.commands.communicator

    def run_session(self):
        session_active = True
        while session_active:
            command_input = self.communicator.get_command()
            if command_input is not None:
                if command_input == "стоп":
                    session_active = False
                    self.communicator.notify_session_end()
                    return
                elif command_input == "рассчитать статистику":
                    self.commands.calculate_statistics()
                elif command_input == "узнать статус пациента":
                    self.commands.get_status_by_id()
                elif command_input == "повысить статус пациента":
                    self.commands.upgrade_status()
                elif command_input == "понизить статус пациента":
                    self.commands.downgrade_status()
                elif command_input == "выписать пациента":
                    self.commands.discharge_patient_()



