from app.communicator import Communicator
from app.custom_exceptions import InvalidIDError, NonExistIDError
from app.hospital import Hospital


class Commands:
    """Use Cases"""

    def __init__(self):
        self.hospital = Hospital()
        self.communicator = Communicator()

    def get_status_by_id(self):
        try:
            index = self._get_and_filter_invalid_id()
            status = self.hospital.get_patient_status(index-1)
            self.communicator.print_patient_status(status)
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)

    def upgrade_status(self):
        try:
            index = self._get_and_filter_invalid_id()
            index -= 1
            if self.hospital.is_patient_valid_for_status_upgrade(index):
                self.hospital.upgrade_status(index)
                self.communicator.print_new_patient_status(self.hospital.get_patient_status(index))
            else:
                if self.communicator.is_patient_ready_for_discharge():
                    self.discharge_patient_(index=index, by_upgrade=True)
                else:
                    self.communicator.notify_status_unchanged()
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)
            return

    def downgrade_status(self):
        try:
            index = self._get_and_filter_invalid_id()
            if index is None:
                return
            index -= 1
            if self.hospital.is_patient_valid_for_status_downgrade(index):
                self.hospital.downgrade_status(index)
                self.communicator.print_new_patient_status(self.hospital.get_patient_status(index))
            else:
                self.communicator.notify_cannot_downgrade_status_error()
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)
            return

    def discharge_patient_(self, index: int = None, by_upgrade: bool = False):
        try:
            if not by_upgrade:
                index = self._get_and_filter_invalid_id()
                print(index)
                if index == -1:
                    return
                index -= 1
            self.hospital.discharge_patient(index)
            self.communicator.notify_patient_is_discharged()
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)
            return

    def calculate_statistics(self):
        patients_amount = self.hospital.calculate_patients_total()
        stat = f'В больнице на данный момент находится {patients_amount} чел., из них: \n'
        for status, amount in self.hospital.get_statistics().items():
            if amount > 0:
                stat += f'   - в статусе "{status}": {amount} чел. \n'
        self.communicator.print_info(stat)

    def _get_and_filter_invalid_id(self) -> int:
        id_input = self.communicator.get_id()
        if not self.hospital.if_id_in_range(id_input) or self.hospital.is_patient_discharged(id_input):
            raise NonExistIDError
        return id_input




