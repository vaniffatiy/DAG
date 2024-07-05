from app.commands import Commands
from app.custom_exceptions import NonExistIDError, InvalidIDError
from unittest.mock import MagicMock, patch

import unittest


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.commands = Commands([1]*10)
        self.hospital = self.commands._hospital
        self.statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Готов к выписке']

    @patch("app.communicator.Communicator.print_info")
    def test_calculate_statistics(self, mock_communicator):
        ex_stat = f'В больнице на данный момент находится 10 чел., из них:\n' \
                  f'   - в статусе "Болен": 10 чел.\n'

        self.commands.calculate_statistics()

        mock_communicator.assert_called_once_with(ex_stat)

    @patch("app.communicator.Communicator.print_info")
    def test_calculate_statistics_after_changes(self, mock_communicator):
        ex_stat = f'В больнице на данный момент находится 9 чел., из них:\n' \
                  f'   - в статусе "Тяжело болен": 1 чел.\n' \
                  f'   - в статусе "Болен": 7 чел.\n' \
                  f'   - в статусе "Слегка болен": 1 чел.\n' \

        self.hospital.upgrade_status(1)
        self.hospital.downgrade_status(2)
        self.hospital.discharge_patient(3)
        self.commands.calculate_statistics()

        mock_communicator.assert_called_once_with(ex_stat)

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.print_new_patient_status")
    def test_upgrade_status_with_valid_value(
        self, mock_notify_status_changed, mock_get_id
    ):
        mock_get_id.return_value = 1
        self.commands.upgrade_status()

        mock_notify_status_changed.assert_called_once_with(self.statuses[2])

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.print_info")
    def test_upgrade_status_with_invalid_value(
        self, mock_print_info, mock_get_id
    ):
        exception = InvalidIDError()
        mock_get_id.return_value = "id"

        self.commands.upgrade_status()

        mock_print_info.assert_called_once_with(exception.args[0])

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.print_info")
    def test_upgrade_status_with_nonexistent_value(
            self, mock_print_info, mock_get_id
    ):
        exception = NonExistIDError()
        mock_get_id.return_value = 201

        self.commands.upgrade_status()

        mock_print_info.assert_called_once_with(exception.args[0])

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.print_new_patient_status")
    def test_upgrade_status_with_patient_valid_for_upgrade(
        self, mock_print_status, mock_get_id
    ):
        mock_get_id.return_value = 1

        self.commands.upgrade_status()

        mock_print_status.assert_called_once_with(self.statuses[2])

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.is_patient_ready_for_discharge")
    @patch("app.communicator.Communicator.notify_patient_is_discharged")
    @patch("app.hospital.Hospital.is_patient_valid_for_status_upgrade")
    def test_upgrade_status_with_patient_valid_for_discharge(
        self, mock_valid_check, mock_notify_discharged, mock_valid_discharge, mock_get_id
    ):
        mock_get_id.return_value = 1
        mock_valid_check.return_value = False
        mock_valid_discharge.return_value = True

        self.commands.upgrade_status()

        mock_notify_discharged.assert_called_once()

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.is_patient_ready_for_discharge")
    @patch("app.communicator.Communicator.notify_status_unchanged")
    @patch("app.hospital.Hospital.is_patient_valid_for_status_upgrade")
    def test_upgrade_status_with_patient_invalid_for_discharge(
        self, mock_valid_check, mock_notify_unchanged, mock_valid_discharge, mock_get_id
    ):
        mock_get_id.return_value = 1
        mock_valid_check.return_value = False
        mock_valid_discharge.return_value = False

        self.commands.upgrade_status()

        mock_notify_unchanged.assert_called_once()

