from app.communicator import Communicator
from app.custom_exceptions import InvalidIDError, IDOffRangeError
from app.hospital import Hospital


class Commands:
    """Use Cases"""

    def __init__(self):
        self.hospital = Hospital()
        self.communicator = Communicator()

    def get_status_by_id(self):
        index = self._get_and_validate_id()
        if index is None:
            return
        status = self.hospital.get_patient_status(index-1)
        self.communicator.print_patient_status(status)

    def upgrade_status(self):
        index = self._get_and_validate_id()
        if index is None:
            return
        index -= 1
        if self.hospital.is_patient_valid_for_status_upgrade(index):
            self.hospital.upgrade_status(index)
            self.communicator.print_new_patient_status(self.hospital.get_patient_status(index))
        else:
            if self.communicator.is_patient_ready_for_discharge():
                self.discharge_patient_(index=index, by_upgrade=True)
            else:
                self.communicator.notify_status_unchanged()

    def downgrade_status(self):
        index = self._get_and_validate_id()
        if index is None:
            return
        index -= 1
        if self.hospital.is_patient_valid_for_status_downgrade(index):
            self.hospital.downgrade_status(index)
            self.communicator.print_new_patient_status(self.hospital.get_patient_status(index))
        else:
            self.communicator.notify_cannot_downgrade_status_error()

    def discharge_patient_(self, index: int = None, by_upgrade: bool = False):
        if not by_upgrade:
            index = self._get_and_validate_id()
            if index is None:
                return
            index -= 1
        self.hospital.discharge_patient(index)
        self.communicator.notify_patient_is_discharged()

    def calculate_statistics(self):
        patients_amount = self.hospital.calculate_patients_total()
        stat = f'В больнице на данный момент находится {patients_amount} чел., из них: \n'
        for i in range(4):
            if self.hospital.is_any_patients(i):
                stat += f'   - в статусе "{self.hospital.get_statistics(i)["status"]}": {self.hospital.get_statistics(i)["amount"]} чел. \n'
        self.communicator.print_statistics(stat)

    def _get_and_filter_invalid_id(self) -> int:
        try:
            id_input = self.communicator.get_id()
            if not self.hospital.if_id_in_range(id_input) or self.hospital.is_patient_discharged(id_input):
                raise IDOffRangeError
            return id_input
        except InvalidIDError:
            self.communicator.notify_id_invalid_error()

    def _get_and_validate_id(self) -> int:
        try:
            id_input = self._get_and_filter_invalid_id()
            return id_input
        except IDOffRangeError:
            self.communicator.notify_id_off_range_error()

