import pytest

from app.custom_exceptions import NonExistIDError
from app.hospital import Hospital


@pytest.fixture()
def statuses():
    return {0: "Тяжело болен", 1: "Болен", 2: "Слегка болен", 3: "Готов к выписке"}


def test_get_patient_status(statuses):
    hospital = Hospital([0, 3, 0])
    assert hospital.get_patient_status(2) == statuses[3]


def test_is_patient_valid_for_status_upgrade():
    hospital = Hospital([0, 3])
    assert hospital.is_patient_valid_for_status_upgrade(1)
    assert not hospital.is_patient_valid_for_status_upgrade(2)


def test_is_patient_valid_for_status_downgrade():
    hospital = Hospital([0, 3])
    assert hospital.is_patient_valid_for_status_downgrade(2)
    assert not hospital.is_patient_valid_for_status_downgrade(1)


def test_upgrade_status():
    hospital = Hospital([0, 2])
    hospital.upgrade_status(2)
    assert hospital._patients_list == [0, 3]


def test_downgrade_status():
    hospital = Hospital([0, 2])
    hospital.downgrade_status(2)
    assert hospital._patients_list == [0, 1]


def test_discharge_patient():
    hospital = Hospital([0, 3])
    hospital.discharge_patient(2)
    assert hospital._patients_list == [0, None]


def test_is_patient_existent():
    hospital = Hospital([1, 3, None])
    assert hospital.is_patient_existent(1)
    try:
        hospital.is_patient_existent(3)
    except NonExistIDError:
        assert True
    try:
        hospital.is_patient_existent(4)
    except NonExistIDError:
        assert True


def test_calculate_patients_total():
    hospital = Hospital([1]*10)
    assert hospital.calculate_patients_total() == 10


def test_get_statistics(statuses):
    hospital = Hospital([1]*20)
    initial_stats = {
        statuses[0]: 0,
        statuses[1]: 20,
        statuses[2]: 0,
        statuses[3]: 0
    }
    assert hospital.get_statistics() == initial_stats


if __name__ == "__main__":
    pytest.main()

