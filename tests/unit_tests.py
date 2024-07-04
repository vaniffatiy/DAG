from unittest.mock import MagicMock, patch
from app.commands import Commands

import unittest

from app.custom_exceptions import NonExistIDError
from app.hospital import Hospital


class TestCalculateStat(unittest.TestCase):
    def setUp(self):
        self.commands = Commands([1]*10)
        self.statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Готов к выписке']

    @patch("app.communicator.Communicator.print_info")
    def test_calculate_statistics(self, mock_communicator):
        hospital = Hospital([1]*10)
        patients = hospital.calculate_patients_total()

        ex_stat = f'В больнице на данный момент находится {patients} чел., из них:\n' \
                  f'   - в статусе "{self.statuses[1]}": {patients} чел.\n'

        self.commands.calculate_statistics()

        mock_communicator.assert_called_once_with(ex_stat)

    @patch("app.communicator.Communicator.print_info")
    def test_calculate_statistics_after_changes(self, mock_communicator):
        hospital = Hospital([1]*10)
        patients = hospital.calculate_patients_total()
        stat = hospital.get_statistics()
        new_stat = {}
        for k, v in stat.items():
            new_stat[k] = v + 1 if k != self.statuses[1] else v - 3
        expected_stat = {
            self.statuses[0]: 1, self.statuses[1]: 7, self.statuses[2]: 1, self.statuses[3]: 1
        }
        ex_stat = f'В больнице на данный момент находится {patients} чел., из них:\n'
        for i in range(4):
            ex_stat += f'   - в статусе "{self.statuses[i]}": {expected_stat[self.statuses[i]]} чел.\n'

        with patch("app.hospital.Hospital.get_statistics", return_value=new_stat) as mock_get_stat:
            self.commands.calculate_statistics()

            mock_get_stat.assert_called_once()
            mock_communicator.assert_called_once_with(ex_stat)


class TestUpgradeStatus(unittest.TestCase):
    def setUp(self):
        self.commands = Commands([1]*10)
        self.statuses = ['Тяжело болен', 'Болен', 'Слегка болен', 'Готов к выписке']

    @patch("app.communicator.Communicator.get_id")
    @patch("app.communicator.Communicator.print_new_patient_status")
    def test_upgrade_status_with_valid_value(
        self, mock_notify_status_changed, mock_get_id
    ):
        mock_get_id.return_value = 1
        self.commands.upgrade_status()

        mock_get_id.assert_called()
        mock_notify_status_changed.assert_called_once_with(self.statuses[2])

    # @patch("app.custom_exceptions.InvalidIDError")
    # @patch("app.communicator.Communicator.get_id")
    # @patch("app.communicator.Communicator.print_info")
    # def test_upgrade_status_with_invalid_value(
    #     self, mock_print_info, mock_get_id, mock_invalid_id_error
    # ):
    #     mock_get_id.side_effect = mock_invalid_id_error
    #     mock_get_id.return_value = -1
    #     self.commands.upgrade_status()
    #
    #     mock_get_id.assert_called()
    #     mock_invalid_id_error.assert_called_once()
    #     mock_print_info.assert_called_once_with(mock_invalid_id_error)
    #
    # @patch("app.communicator.Communicator.get_id")
    # @patch("app.custom_exceptions.NonExistIDError")
    # @patch("app.communicator.Communicator.print_info")
    # def test_upgrade_status_with_nonexistent_value(
    #         self, mock_print_info, mock_nonexist_id_error, mock_get_id
    # ):
    #     mock_get_id = 201
    #
    #     self.commands.upgrade_status()
    #
    #
    #     mock_get_id.assert_called()
    #     mock_print_info.assert_called_once_with(NonExistIDError())  # Здесь мы вызываем без аргументов
    #
    #
    #     assert str(mock_print_info.call_args[0][0]) == "Ошибка. В больнице нет пациента с таким ID"
    #
    # @patch("app.commands.Commands._get_and_filter_invalid_id")
    # @patch("app.communicator.Communicator.print_new_patient_status")
    # @patch("app.hospital.Hospital")
    # def test_upgrade_status_with_patient_valid_for_upgrade(
    #     self, mock_hospital, mock_communicator, mock_get_id
    # ):
    #     mock_get_id.return_value = 1
    #     index = mock_get_id.return_value - 1
    #     mock_hospital.is_patient_valid_for_status_upgrade.return_value = True
    #     mock_hospital.get_patient_status.return_value = self.statuses[2]
    #
    #     self.commands.upgrade_status()
    #
    #     mock_get_id.assert_called()
    #     mock_hospital.is_patient_valid_for_status_upgrade.assert_called_once_with(index)
    #     mock_hospital.upgrade_status.assert_called_once_with(index)
    #     mock_communicator.assert_called_once_with(self.statuses[2])
    #
    # @patch("app.commands.Commands._get_and_filter_invalid_id")
    # @patch("app.communicator.Communicator")
    # @patch("app.hospital.Hospital")
    # def test_upgrade_status_with_patient_valid_for_discharge(
    #     self, mock_hospital, mock_communicator, mock_get_id
    # ):
    #     mock_get_id.return_value = 1
    #     index = mock_get_id.return_value-1
    #     mock_hospital.return_value.is_patient_valid_for_status_upgrade.return_value = False
    #     mock_communicator.is_patient_ready_for_discharge.return_value = True
    #
    #     self.commands.upgrade_status()
    #
    #     mock_get_id.assert_called_once()
    #     mock_hospital.is_patient_valid_for_status_upgrade.assert_called_once_with(index)
    #     mock_hospital.is_patient_ready_for_discharge.assert_called_once_with(index)
    #     mock_hospital.discharge_patient.assert_called_once_with(index=index, by_upgrade=True)
    #     mock_communicator.notify_patient_is_discharged.assert_called_once()
    #
    # @patch("app.commands.Commands._get_and_filter_invalid_id")
    # @patch("app.communicator.Communicator")
    # @patch("app.hospital.Hospital")
    # def test_upgrade_status_with_patient_invalid_for_discharge(
    #     self, mock_hospital, mock_communicator, mock_get_id
    # ):
    #     mock_get_id.return_value = 1
    #     index = mock_get_id.return_value - 1
    #     mock_hospital.return_value.is_patient_valid_for_status_upgrade.return_value = False
    #     mock_communicator.is_patient_ready_for_discharge.return_value = False
    #
    #     self.commands.upgrade_status()
    #
    #     mock_get_id.assert_called_once()
    #     mock_hospital.is_patient_valid_for_status_upgrade.assert_called_once_with(index)
    #     mock_hospital.is_patient_ready_for_discharge.assert_called_once_with(index)
    #     mock_communicator.notify_status_unchanged.assert_called_once()


if __name__ == "__main__":
    unittest.main()
