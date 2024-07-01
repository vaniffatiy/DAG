from unittest.mock import MagicMock, patch
from app.commands import Commands

import unittest


class TestCalculateStat(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()
        self.statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Готов к выписке']

    @patch("app.communicator.Communicator.print_info")
    @patch("app.hospital.Hospital.calculate_patients_total")
    @patch("app.hospital.Hospital.get_statistics")
    def test_with_regular_values(self, mock_get_stat, mock_count_patients, mock_communicator):
        mock_count_patients.return_value = 195
        mock_get_stat.return_value = {
            self.statuses[0]: 10, self.statuses[1]: 180, self.statuses[2]: 0, self.statuses[3]: 5
        }
        stat = f'В больнице на данный момент находится {mock_count_patients.return_value} чел., из них:\n'\
               f'   - в статусе "{self.statuses[0]}": {mock_get_stat.return_value[self.statuses[0]]} чел.\n' \
               f'   - в статусе "{self.statuses[1]}": {mock_get_stat.return_value[self.statuses[1]]} чел.\n' \
               f'   - в статусе "{self.statuses[3]}": {mock_get_stat.return_value[self.statuses[3]]} чел.\n'

        self.commands.calculate_statistics()

        mock_count_patients.assert_called_once()
        mock_get_stat.assert_called_once()
        mock_communicator.assert_called_once_with(stat)


class TestUpgradeStatus(unittest.TestCase):
    def setUp(self):
        # self.mock_get_id = mock.MagicMock()
        # self.mock_invalid_id_error = mock.MagicMock()
        # self.mock_nonexist_id_error = mock.MagicMock()
        # self.mock_print_info = mock.MagicMock()
        # self.mock_communicator = mock.MagicMock()
        # self.mock_hospital = mock.MagicMock()
        self.commands = Commands()
        self.statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Готов к выписке']

    @patch("app.custom_exceptions.InvalidIDError")
    @patch("app.commands.Commands._get_and_filter_invalid_id")
    @patch("app.communicator.Communicator.print_info")
    def test_upgrade_status_with_invalid_value(
        self, mock_print_info, mock_get_id, mock_invalid_id_error
    ):
        mock_get_id.side_effect = mock_invalid_id_error

        self.commands.upgrade_status()

        mock_get_id.assert_called()
        mock_invalid_id_error.assert_called_once()
        mock_print_info.assert_called_once_with(mock_invalid_id_error)

    @patch("app.commands.Commands._get_and_filter_invalid_id")
    @patch("app.custom_exceptions.NonExistIDError")
    @patch("app.communicator.Communicator.print_info")
    def test_upgrade_status_with_nonexistent_value(
        self, mock_communicator, mock_nonexist_id_error, mock_get_id
    ):
        mock_get_id.side_effect = mock_nonexist_id_error

        self.commands.upgrade_status()

        mock_get_id.assert_called()
        mock_nonexist_id_error.assert_called_once()
        mock_communicator.assert_called_once_with(mock_nonexist_id_error)

    @patch("app.commands.Commands._get_and_filter_invalid_id")
    @patch("app.communicator.Communicator.print_new_patient_status")
    @patch("app.hospital.Hospital")
    def test_upgrade_status_with_patient_valid_for_upgrade(
        self, mock_hospital, mock_communicator, mock_get_id
    ):
        mock_get_id.return_value = 1
        index = mock_get_id.return_value - 1
        mock_hospital.is_patient_valid_for_status_upgrade.return_value = True
        mock_hospital.get_patient_status.return_value = self.statuses[2]

        self.commands.upgrade_status()

        mock_get_id.assert_called()
        mock_hospital.is_patient_valid_for_status_upgrade.assert_called_once_with(index)
        mock_hospital.upgrade_status.assert_called_once_with(index)
        mock_communicator.assert_called_once_with(self.statuses[2])

    @patch("app.commands.Commands._get_and_filter_invalid_id")
    @patch("app.communicator.Communicator")
    @patch("app.hospital.Hospital")
    def test_upgrade_status_with_patient_valid_for_discharge(
        self, mock_hospital, mock_communicator, mock_get_id
    ):
        mock_get_id.return_value = 1
        index = mock_get_id.return_value-1
        mock_hospital.return_value.is_patient_valid_for_status_upgrade.return_value = False
        mock_communicator.is_patient_ready_for_discharge.return_value = True

        self.commands.upgrade_status()

        mock_get_id.assert_called_once()
        mock_hospital.is_patient_valid_for_status_upgrade.assert_called_once_with(index)
        mock_hospital.is_patient_ready_for_discharge.assert_called_once_with(index)
        mock_hospital.discharge_patient.assert_called_once_with(index=index, by_upgrade=True)
        mock_communicator.notify_patient_is_discharged.assert_called_once()

    @patch("app.commands.Commands._get_and_filter_invalid_id")
    @patch("app.communicator.Communicator")
    @patch("app.hospital.Hospital")
    def test_upgrade_status_with_patient_invalid_for_discharge(
        self, mock_hospital, mock_communicator, mock_get_id
    ):
        mock_get_id.return_value = 1
        index = mock_get_id.return_value - 1
        mock_hospital.return_value.is_patient_valid_for_status_upgrade.return_value = False
        mock_communicator.is_patient_ready_for_discharge.return_value = False

        self.commands.upgrade_status()

        mock_get_id.assert_called_once()
        mock_hospital.is_patient_valid_for_status_upgrade.assert_called_once_with(index)
        mock_hospital.is_patient_ready_for_discharge.assert_called_once_with(index)
        mock_communicator.notify_status_unchanged.assert_called_once()


if __name__ == "__main__":
    unittest.main()
