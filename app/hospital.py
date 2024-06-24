from app.data_manager import DataManager


class Hospital:
    def __init__(self):
        self.data_manager = DataManager()
        """Entity"""

    def get_patient_status(self, index: int) -> str:
        status_index = self.data_manager.get_status(index)
        return self.data_manager.get_status_name(status_index)

    def is_patient_valid_for_status_change(self, index: int, upgrade: bool = True):
        if upgrade:
            return self.data_manager.get_status(index) < 3
        else:
            return self.data_manager.get_status(index) > 0

    def change_patient_status(self, index: int, upgrade: bool = True):
        if upgrade:
            self.data_manager.patients_list[index] += 1
        else:
            self.data_manager.patients_list[index] -= 1

    def discharge_patient(self, index: int):
        self.data_manager.patients_list[index] = None

    def filter_id_values(self, id: str) -> str:
        if not id.isdigit() or int(id) < 0:
            response = "invalid"
        elif int(id) not in range(201) or self.data_manager.get_status(int(id)-1) is None:
            response = "off_range"
        else:
            response = "OK"
        return response

    def verify_command_type(self, command: str, request: str) -> bool:
        return self.data_manager.verify_command_type(command, request)

    def calculate_patients_by_status(self, status: int) -> int:
        filtered_list = []
        for patient_status in self.data_manager.patients_list:
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
        patients = [patient for patient in self.data_manager.patients_list if patient is not None]
        return len(patients)

    def is_any_patients(self, index: int) -> bool:
        return self.calculate_patients_by_status(index) > 0

    def get_statistics(self, index: int) -> dict:
        stat = {"status": self.data_manager.get_status_name(index), "amount": self.calculate_patients_by_status(index)}
        return stat
