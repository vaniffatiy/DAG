import pytest

from app.communicator import Communicator
from app.custom_exceptions import InvalidIDError


@pytest.fixture
def communicator():
    communicator = Communicator()
    return communicator


class TestCommunicator:
    def test_get_command(self, mocker, communicator):
        mock_input = mocker.patch("builtins.input", return_value="status UP")
        response = communicator.get_command()
        assert response == "повысить статус пациента"

    def test_get_unknown_command(self, mocker, communicator):
        mock_input = mocker.patch("builtins.input", return_value="status")
        mock_print = mocker.patch("builtins.print")

        communicator.get_command()

        mock_print.assert_called_once_with("Неизвестная команда! Попробуйте ещё раз")

    def test_get_valid_id(self, mocker, communicator):
        mock_input = mocker.patch("builtins.input", return_value="2")
        response = communicator.get_id()
        assert response == 2

    def test_get_invalid_id(self, mocker, communicator):
        mock_input = mocker.patch("builtins.input", return_value="id")
        with pytest.raises(InvalidIDError):
            communicator.get_id()

    def test_is_patient_ready_for_discharge(self, mocker, communicator):
        mock_input = mocker.patch("builtins.input", return_value="да")
        response = communicator.is_patient_ready_for_discharge()
        assert response is True

    def test_is_patient_ready_for_discharge_negative(self, mocker, communicator):
        mock_input = mocker.patch("builtins.input", return_value="yes")
        response = communicator.is_patient_ready_for_discharge()
        assert response is False

    def test_notify_cannot_downgrade_status_error(self, mocker, communicator):
        mock_print = mocker.patch("builtins.print")
        communicator.notify_status_unchanged()
        mock_print.assert_called_once_with('Пациент остался в статусе "Готов к выписке"')

