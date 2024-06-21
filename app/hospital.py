from app.data import patients_list, statuses_dict, commands_dict


class Hospital:
    """Entity"""

    def get_patient_status(self, index: int) -> str:
        status_index = patients_list[index]
        return statuses_dict[status_index]

    def is_patient_valid_for_status_change(self, index: int, upgrade: bool = True):
        if upgrade:
            return patients_list[index] < 3
        else:
            return patients_list[index] > 0

    def change_patient_status(self, index: int, upgrade: bool = True):
        if upgrade:
            patients_list[index] += 1
        else:
            patients_list[index] -= 1

    def discharge_patient(self, index: int):
        patients_list[index] = None

    def filter_id_values(self, id: str) -> str:
        if not id.isdigit() or int(id) < 0:
            response = "invalid"
        elif int(id) not in range(201) or patients_list[int(id)-1] is None:
            response = "off_range"
        else:
            response = "OK"
        return response

    def verify_command_type(self, command: str, request: str) -> bool:
        if request == "stop":
            return command in commands_dict["стоп"]
        elif request == "calculate":
            return command in commands_dict["рассчитать"]
        elif request == "check":
            return command in commands_dict["узнать"]
        elif request == "upgrade":
            return command in commands_dict["повысить"]
        elif request == "downgrade":
            return command in commands_dict["понизить"]
        elif request == "discharge":
            return command in commands_dict["выписать"]
        elif request == "any_valid":
            found = False
            for c in commands_dict:
                if command in commands_dict[c]:
                    found = True
            return found

    def calculate_patients_by_status(self, status: int) -> int:
        filtered_list = []
        for patient_status in patients_list:
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
        patients = [patient for patient in patients_list if patient is not None]
        return len(patients)

    def is_any_patients(self, index: int) -> bool:
        return self.calculate_patients_by_status(index) > 0

    def get_statistics(self, index: int) -> dict:
        stat = {"status": statuses_dict[index], "amount": self.calculate_patients_by_status(index)}
        return stat
