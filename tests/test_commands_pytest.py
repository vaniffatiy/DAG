from app.commands import Commands


class TestCommands:
    def test_calculate_statistics(self, mocker):
        commands = Commands([1] * 10)
        mock_communicator = mocker.patch("app.communicator.Communicator.print_info")
        ex_stat = f'В больнице на данный момент находится 10 чел., из них:\n' \
                  f'   - в статусе "Болен": 10 чел.\n'

        commands.calculate_statistics()

        mock_communicator.assert_called_once_with(ex_stat)

    def test_calculate_statistics_after_changes(self, mocker):
        commands = Commands([1] * 10)
        hospital = commands.hospital
        mock_communicator = mocker.patch("app.communicator.Communicator.print_info")
        ex_stat = f'В больнице на данный момент находится 9 чел., из них:\n' \
                  f'   - в статусе "Тяжело болен": 1 чел.\n' \
                  f'   - в статусе "Болен": 7 чел.\n' \
                  f'   - в статусе "Слегка болен": 1 чел.\n'

        hospital.upgrade_status(1)
        hospital.downgrade_status(2)
        hospital.discharge_patient(3)
        commands.calculate_statistics()

        mock_communicator.assert_called_once_with(ex_stat)

    def test_upgrade_status_with_valid_value(self, mocker):
        commands = Commands([1, 2])
        mock_notify_status_changed = mocker.patch("app.communicator.Communicator.print_new_patient_status")
        mock_get_id = mocker.patch("app.communicator.Communicator.get_id")
        mock_get_id.return_value = 1

        commands.upgrade_status()

        assert commands.hospital._patients_list == [2, 2]
        mock_notify_status_changed.assert_called_once_with("Слегка болен")

    def test_upgrade_status_with_invalid_value(self, mocker):
        commands = Commands([1, 2])
        mock_print_info = mocker.patch("app.communicator.Communicator.print_info")
        mock_get_id = mocker.patch("app.communicator.Communicator.get_id")
        mock_get_id.return_value = "id"

        commands.upgrade_status()

        assert commands.hospital._patients_list == [1, 2]
        mock_print_info.assert_called_once_with('Ошибка. ID пациента должно быть числом (целым, положительным)')

    def test_upgrade_status_with_nonexistent_value(self, mocker):
        commands = Commands([1, 2])
        mock_print_info = mocker.patch("app.communicator.Communicator.print_info")
        mock_get_id = mocker.patch("app.communicator.Communicator.get_id")
        mock_get_id.return_value = 201

        commands.upgrade_status()

        assert commands.hospital._patients_list == [1, 2]
        mock_print_info.assert_called_once_with('Ошибка. В больнице нет пациента с таким ID')

    def test_upgrade_status_with_patient_valid_for_discharge(self, mocker):
        commands = Commands([1, 2])
        mock_valid_check = mocker.patch("app.hospital.Hospital.is_patient_valid_for_status_upgrade")
        mock_notify_discharged = mocker.patch("app.communicator.Communicator.notify_patient_is_discharged")
        mock_valid_discharge = mocker.patch("app.communicator.Communicator.is_patient_ready_for_discharge")
        mock_get_id = mocker.patch("app.communicator.Communicator.get_id")
        mock_get_id.return_value = 1
        mock_valid_check.return_value = False
        mock_valid_discharge.return_value = True

        commands.upgrade_status()

        assert commands.hospital._patients_list == [None, 2]
        mock_notify_discharged.assert_called_once()

    def test_upgrade_status_with_patient_invalid_for_discharge(self, mocker):
        commands = Commands([1, 2])
        mock_valid_check = mocker.patch("app.hospital.Hospital.is_patient_valid_for_status_upgrade")
        mock_notify_unchanged = mocker.patch("app.communicator.Communicator.notify_status_unchanged")
        mock_valid_discharge = mocker.patch("app.communicator.Communicator.is_patient_ready_for_discharge")
        mock_get_id = mocker.patch("app.communicator.Communicator.get_id")
        mock_get_id.return_value = 1
        mock_valid_check.return_value = False
        mock_valid_discharge.return_value = False

        commands.upgrade_status()

        assert commands.hospital._patients_list == [1, 2]
        mock_notify_unchanged.assert_called_once()

