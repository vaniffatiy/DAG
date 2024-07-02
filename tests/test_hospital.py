import pytest
from tests import steps


@pytest.fixture()
def statuses():
    return {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}


def test_get_patient_status(statuses):
    steps.verify_patient_status(0, statuses[1])
    steps.upgrade_status(0)
    steps.verify_patient_status(0, statuses[2])


def test_is_patient_valid_for_status_upgrade():
    steps.verify_patient_valid_for_upgrade(0)
    steps.upgrade_status(0)
    steps.verify_patient_valid_for_upgrade(0)
    steps.upgrade_status(0)
    steps.verify_patient_not_valid_for_upgrade(0)


def test_is_patient_valid_for_status_downgrade():
    steps.verify_patient_valid_for_downgrade(0)
    steps.downgrade_status(0)
    steps.verify_patient_not_valid_for_downgrade(0)


def test_upgrade_status(statuses):
    steps.verify_patient_status(0, statuses[1])
    steps.upgrade_status(0)
    steps.verify_patient_status(0, statuses[2])


def test_downgrade_status(statuses):
    steps.verify_patient_status(0, statuses[1])
    steps.downgrade_status(0)
    steps.verify_patient_status(0, statuses[0])


def test_discharge_patient():
    steps.discharge_patient(0)
    steps.verify_patient_is_discharged(0)


def test_is_patient_discharged():
    steps.verify_patient_is_not_discharged(0)
    steps.verify_patient_is_not_discharged(1)
    steps.discharge_patient(0)
    steps.verify_patient_is_discharged(0)
    steps.verify_patient_is_not_discharged(1)


def test_if_id_in_range():
    steps.verify_id_is_in_range(1)
    steps.verify_id_is_not_in_range(-1)
    steps.verify_id_is_in_range(200)
    steps.verify_id_is_not_in_range(201)


def test_calculate_patients_total():
    steps.verify_patients_amount(200)
    steps.discharge_patient(0)
    steps.verify_patients_amount(199)


def test_get_statistics(statuses):
    initial_stats = {
        statuses[0]: 0,
        statuses[1]: 200,
        statuses[2]: 0,
        statuses[3]: 0
    }
    steps.verify_statistics_is_correct(initial_stats)

    steps.upgrade_status(0)
    steps.upgrade_status(1)
    steps.upgrade_status(1)
    steps.downgrade_status(2)

    updated_stats = {k: v + 1 for k, v in initial_stats.items()}
    updated_stats[statuses[1]] = 197
    steps.verify_statistics_is_correct(updated_stats)



