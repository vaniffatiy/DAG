from app.custom_exceptions import NonExistIDError


class Hospital:
    """Entity"""
    def __init__(self, patients_list=None):
        self._patients_list = patients_list
        self._statuses_dict = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def get_patient_status(self, id_input: int) -> str:
        if self.is_patient_existent(id_input):
            status_index = self._patients_list[id_input-1]
            return self._statuses_dict[status_index]

    def is_patient_valid_for_status_upgrade(self, id_input: int) -> bool:
        if self.is_patient_existent(id_input):
            return self._patients_list[id_input-1] < 3

    def is_patient_valid_for_status_downgrade(self, id_input: int) -> bool:
        if self.is_patient_existent(id_input):
            return self._patients_list[id_input-1] > 0

    def upgrade_status(self, id_input: int):
        if self.is_patient_existent(id_input):
            self._patients_list[id_input-1] += 1

    def downgrade_status(self, id_input: int):
        if self.is_patient_existent(id_input):
            self._patients_list[id_input-1] -= 1

    def discharge_patient(self, id_input: int):
        if self.is_patient_existent(id_input):
            self._patients_list[id_input-1] = None

    def _is_patient_discharged(self, index: int):
        return self._patients_list[index] is None

    def _is_id_in_range(self, id_input: int) -> bool:
        return id_input in range(len(self._patients_list)+1)

    def is_patient_existent(self, id_input: int) -> bool:
        if not self._is_id_in_range(id_input) or self._is_patient_discharged(id_input-1):
            raise NonExistIDError
        return True

    def calculate_patients_total(self) -> int:
        return sum(1 for patient in self._patients_list if patient is not None)

    def get_statistics(self) -> dict:
        stat = {}
        for i in range(4):
            stat[self._statuses_dict[i]] = 0
        for i in self._patients_list:
            stat[self._statuses_dict[i]] += 1
        return stat

