class Hospital:
    """Entity"""
    def __init__(self):
        self._patients_list = [1]*200
        self._statuses_dict = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def get_patient_status(self, index: int) -> str:
        status_index = self._patients_list[index]
        return self._statuses_dict[status_index]

    def is_patient_valid_for_status_upgrade(self, index: int):
        print(self._patients_list[index])
        return self._patients_list[index] < 3

    def is_patient_valid_for_status_downgrade(self, index: int):
        return self._patients_list[index] > 0

    def upgrade_status(self, index: int):
        self._patients_list[index] += 1

    def downgrade_status(self, index: int):
        self._patients_list[index] -= 1

    def discharge_patient(self, index: int):
        self._patients_list[index] = None

    def is_patient_discharged(self, id_input: int):
        return self._patients_list[id_input-1] is None

    def if_id_in_range(self, id_input: int) -> bool:
        return id_input in range(len(self._patients_list)+1)

    def _calculate_patients_by_status(self, status: int) -> int:
        filtered_list = []
        for patient_status in self._patients_list:
            if status == patient_status:
                filtered_list.append(patient_status)
        return len(filtered_list)

    def calculate_patients_total(self) -> int:
        patients = [patient for patient in self._patients_list if patient is not None]
        return len(patients)

    def is_any_patients(self, index: int) -> bool:
        return self._calculate_patients_by_status(index) > 0

    def get_statistics(self, index: int) -> dict:
        stat = {"status": self._statuses_dict[index], "amount": self._calculate_patients_by_status(index)}
        return stat
