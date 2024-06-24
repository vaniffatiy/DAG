from app.communicator import Communicator
from app.hospital import Hospital


class Commands:
    """Use Cases"""

    def __init__(self):
        self.hospital = Hospital()
        self.communicator = Communicator()

    def get_status_by_id(self, index: int):
        status = self.hospital.get_patient_status(index)
        self.communicator.print_patient_status(status)

    def upgrade_status(self, index: int):
        if self.hospital.is_patient_valid_for_status_change(index):
            self.hospital.change_patient_status(index)
            self.communicator.print_new_patient_status(self.hospital.get_patient_status(index))
        else:
            if self.communicator.is_patient_ready_for_discharge():
                self.discharge_patient(index)
            else:
                self.communicator.notify_status_unchanged()

    def downgrade_status(self, index: int):
        if self.hospital.is_patient_valid_for_status_change(index, upgrade=False):
            self.hospital.change_patient_status(index, upgrade=False)
            self.communicator.print_new_patient_status(self.hospital.get_patient_status(index))
        else:
            self.communicator.notify_cannot_downgrade_status_error()

    def discharge_patient(self, index: int):
        self.hospital.discharge_patient(index)
        self.communicator.notify_patient_is_discharged()

    def calculate_statistics(self):
        patients_amount = self.hospital.calculate_patients_total()
        stat = f'В больнице на данный момент находится {patients_amount} чел., из них: \n'
        for i in range(4):
            if self.hospital.is_any_patients(i):
                stat += f'   - в статусе "{self.hospital.get_statistics(i)["status"]}": {self.hospital.get_statistics(i)["amount"]} чел. \n'
        self.communicator.print_statistics(stat)


