from app.commands import Commands

commands = Commands()
hospital = commands.hospital


def verify_patient_status(index: int, status: str):
    assert hospital.get_patient_status(index) == status, (
        "Статус пациента не соответствует ожидаемому"
    )


def verify_patient_valid_for_upgrade(index: int):
    assert hospital.is_patient_valid_for_status_upgrade(index), (
        "Статус пациента невозможно поднять"
    )


def verify_patient_not_valid_for_upgrade(index: int):
    assert not hospital.is_patient_valid_for_status_upgrade(index), (
        "Статус пациента можно поднять"
    )


def verify_patient_valid_for_downgrade(index: int):
    assert hospital.is_patient_valid_for_status_downgrade(index), (
        "Статус пациента невозможно снизить"
    )


def verify_patient_not_valid_for_downgrade(index: int):
    assert not hospital.is_patient_valid_for_status_downgrade(index), (
        "Статус пациента можно снизить"
    )


def verify_patient_is_discharged(index: int):
    assert hospital.is_patient_discharged(index), (
        "Пациент не выписан из больницы"
    )


def verify_patient_is_not_discharged(index: int):
    assert not hospital.is_patient_discharged(index), (
        "Пациент выписан из больницы"
    )


def verify_id_is_in_range(id_input: int):
    assert hospital.is_id_in_range(id_input), (
        "ID вне диапазона, такого пациента не существует"
    )


def verify_id_is_not_in_range(id_input: int):
    assert not hospital.is_id_in_range(id_input), (
        "ID в диапазоне, такой пациент существует"
    )


def verify_patients_amount(amount: int):
    assert hospital.calculate_patients_total() == amount, (
        "Количество пациентов в больнице не соответствует ожидаемому"
    )


def verify_statistics_is_correct(stat: dict):
    assert hospital.get_statistics() == stat, (
        "Статистика собрана некорректно"
    )


def upgrade_status(index: int):
    hospital.upgrade_status(index)


def downgrade_status(index: int):
    hospital.downgrade_status(index)


def discharge_patient(index:int):
    hospital.discharge_patient(index)