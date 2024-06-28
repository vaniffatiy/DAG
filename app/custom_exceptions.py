class InvalidIDError(Exception):
    def __init__(self, message="Ошибка. ID пациента должно быть числом (целым, положительным)"):
        super().__init__(message)


class NonExistIDError(Exception):
    def __init__(self, message="Ошибка. В больнице нет пациента с таким ID"):
        super().__init__(message)
