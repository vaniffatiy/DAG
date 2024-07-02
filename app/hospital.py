class Hospital:
    """Entity"""
    def __init__(self):
        self._patients_list = [1]*200
        self._statuses_dict = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def get_patient_status(self, index: int) -> str:
        status_index = self._patients_list[index]
        return self._statuses_dict[status_index]

    def is_patient_valid_for_status_upgrade(self, index: int):
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

    def calculate_patients_total(self) -> int:
        return sum(1 for patient in self._patients_list if patient is not None)

    def get_statistics(self) -> dict:
        stat = {}
        for i in range(4):
            stat[self._statuses_dict[i]] = 0
        for i in self._patients_list:
            stat[self._statuses_dict[i]] += 1
        return stat

