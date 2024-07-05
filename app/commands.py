from app.communicator import Communicator
from app.custom_exceptions import InvalidIDError, NonExistIDError
from app.hospital import Hospital


class Commands:
    """Use Cases"""

    def __init__(self, _patients: list = [1]*200):
        self._hospital = Hospital(_patients)
        self.communicator = Communicator()

    def get_status_by_id(self):
        try:
            id_input = self.communicator.get_id()
            status = self._hospital.get_patient_status(id_input)
            self.communicator.print_patient_status(status)
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)

    def upgrade_status(self):
        try:
            id_input = self.communicator.get_id()
            if self._hospital.is_patient_valid_for_status_upgrade(id_input):
                self._hospital.upgrade_status(id_input)
                self.communicator.print_new_patient_status(self._hospital.get_patient_status(id_input))
            else:
                if self.communicator.is_patient_ready_for_discharge():
                    self.discharge_patient_(id_input=id_input, by_upgrade=True)
                else:
                    self.communicator.notify_status_unchanged()
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err.args[0])
            return

    def downgrade_status(self):
        try:
            id_input = self.communicator.get_id()
            if self._hospital.is_patient_valid_for_status_downgrade(id_input):
                self._hospital.downgrade_status(id_input)
                self.communicator.print_new_patient_status(self._hospital.get_patient_status(id_input))
            else:
                self.communicator.notify_cannot_downgrade_status_error()
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)
            return

    def discharge_patient_(self, id_input: int = None, by_upgrade: bool = False):
        try:
            if not by_upgrade:
                id_input = self.communicator.get_id()
            self._hospital.discharge_patient(id_input)
            self.communicator.notify_patient_is_discharged()
        except (InvalidIDError, NonExistIDError) as err:
            self.communicator.print_info(err)
            return

    def calculate_statistics(self):
        patients_amount = self._hospital.calculate_patients_total()
        stat = f'В больнице на данный момент находится {patients_amount} чел., из них:\n'
        for status, amount in self._hospital.get_statistics().items():
            if amount > 0:
                stat += f'   - в статусе "{status}": {amount} чел.\n'
        self.communicator.print_info(stat)





