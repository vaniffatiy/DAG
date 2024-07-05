import pytest

from app.custom_exceptions import NonExistIDError
from app.hospital import Hospital


def test_get_patient_status():
    hospital = Hospital([0, 3, 0])
    assert hospital.get_patient_status(2) == "Готов к выписке"


def test_cannot_get_patient_status():
    hospital = Hospital([0, 3, 0])
    with pytest.raises(NonExistIDError):
        hospital.get_patient_status(4)


def test_is_patient_valid_for_status_upgrade():
    hospital = Hospital([0, 3])
    assert hospital.is_patient_valid_for_status_upgrade(1)


def test_is_patient_not_valid_for_status_upgrade():
    hospital = Hospital([0, 3])
    assert not hospital.is_patient_valid_for_status_upgrade(2)


def test_is_patient_valid_for_status_downgrade():
    hospital = Hospital([0, 3])
    assert hospital.is_patient_valid_for_status_downgrade(2)


def test_is_patient_not_valid_for_status_downgrade():
    hospital = Hospital([0, 3])
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


def test_is_patient_not_existent_discharged():
    hospital = Hospital([1, 3, None])
    with pytest.raises(NonExistIDError):
        hospital.is_patient_existent(3)


def test_is_patient_not_existent_off_range():
    hospital = Hospital([1, 3, None])
    with pytest.raises(NonExistIDError):
        hospital.is_patient_existent(4)


def test_calculate_patients_total():
    hospital = Hospital([1, 2, None, 3])
    assert hospital.calculate_patients_total() == 3


def test_get_statistics():
    hospital = Hospital([0, 1, 1, 2, None, 1, 2, 3])
    statistics = {
        "Тяжело болен": 1,
        "Болен": 3,
        "Слегка болен": 2,
        "Готов к выписке": 1
    }
    assert hospital.get_statistics() == statistics


