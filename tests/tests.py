class AcceptanceTests:
    def __init__(self, app):
        self.app = app
        self.run = self.app.run_commands
    """
    ввод дополнительных данных и проверка тестов происходят вручную
    """

    def test_base_scenario(self):
        self.run.process_command("повысить статус пациента", id=200)
        self.run.process_command("status up", id=2)
        self.run.process_command("status down", id=3)
        self.run.process_command("discharge", id=4)
        self.run.process_command("рассчитать статистику")
        self.run.process_command("стоп")

    def test_unknown_command(self):
        self.run.process_command("выписать всех пациентов")
        self.run.process_command("стоп")

    def test_various_inputs(self):
        self.run.process_command("узнать статус пациента", id=7)
        self.run.process_command("GET STATUS", id=7)
        self.run.process_command("Узнать СТАТУС пациентА", id=7)
        self.run.process_command("стоп")

    def test_invalid_input(self):
        self.run.process_command("узнать статус пациента", id="два")
        self.run.process_command("повысить статус пациента", id=-2)
        self.run.process_command("понизить статус пациента", id=201)
        self.run.process_command("стоп")

    def test_upgrade_highest_status_to_discharge(self):
        self.run.process_command("повысить статус пациента", id=1)
        self.run.process_command("повысить статус пациента", id=1)
        self.run.process_command("повысить статус пациента", id=1)
        """ввести 'да'."""
        self.run.process_command("рассчитать статистику")
        self.run.process_command("стоп")

    def test_upgrade_highest_status_without_change(self):
        self.run.process_command("повысить статус пациента", id=1)
        self.run.process_command("повысить статус пациента", id=1)
        self.run.process_command("повысить статус пациента", id=1)
        """ввести 'нет'."""
        self.run.process_command("рассчитать статистику")
        self.run.process_command("стоп")

    def test_fail_to_downgrade_lowest_status(self):
        self.run.process_command("понизить статус пациента", id=1)
        self.run.process_command("понизить статус пациента", id=1)
        self.run.process_command("рассчитать статистику")
        self.run.process_command("стоп")



