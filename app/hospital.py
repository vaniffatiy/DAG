pat_list = [1]*200


class Hospital:
    """Entity"""
    def __init__(self):
        self._patients_list = pat_list
        self._statuses_dict = {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}

    def get_patient_status(self, index: int) -> str:
        status_index = self._patients_list[index]
        return self._statuses_dict[status_index]

    def is_patient_valid_for_status_change(self, index: int, upgrade: bool = True):
        if upgrade:
            return self._patients_list[index] < 3
        else:
            return self._patients_list[index] > 0

    def change_patient_status(self, index: int, upgrade: bool = True):
        if upgrade:
            self._patients_list[index] += 1
        else:
            self._patients_list[index] -= 1

    def discharge_patient(self, index: int):
        self._patients_list[index] = None

    def is_patient_discharged(self, index: int):
        return self._patients_list[index] is None

    def calculate_patients_by_status(self, status: int) -> int:
        filtered_list = []
        for patient_status in self._patients_list:
            if status == 0 and patient_status == 0:
                filtered_list.append(patient_status)
            if status == 1 and patient_status == 1:
                filtered_list.append(patient_status)
            if status == 2 and patient_status == 2:
                filtered_list.append(patient_status)
            if status == 3 and patient_status == 3:
                filtered_list.append(patient_status)
        return len(filtered_list)

    def calculate_patients_total(self) -> int:
        patients = [patient for patient in self._patients_list if patient is not None]
        return len(patients)

    def is_any_patients(self, index: int) -> bool:
        return self.calculate_patients_by_status(index) > 0

    def get_statistics(self, index: int) -> dict:
        stat = {"status": self._statuses_dict[index], "amount": self.calculate_patients_by_status(index)}
        return stat
