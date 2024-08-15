class Car:
    def __init__(self, model: str, _vin: int, __number: str):
        self.model = model
        self._vin = self.__is_valid_vin(_vin)
        self.__number = self.__is_valid_numbers(__number)
        if self._vin and self.__number:
            print(f'{self.model} was successfully added')

    def __is_valid_vin(self, vin_number):
        try:
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber(f'{self.model} - Incorrect VIN type. It must be INT but not', type(vin_number))
            elif not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber(f'{self.model} - Incorrect VIN range. It must be between 1000000 and '
                                         f'9999999, gotten',
                                         vin_number)

            return True
        except IncorrectVinNumber as exc:
            print(exc.message, exc.data)
            return False

    def __is_valid_numbers(self, number):
        try:
            if not isinstance(number, str):
                raise IncorrectCarNumber(f'{self.model} - Incorrect Car number. It must be STR but not', type(number))
            elif len(number) != 6:
                raise IncorrectCarNumber(f'{self.model} - Incorrect Car number length. It must be 6 symbols, gotten',
                                         len(number))

            return True
        except IncorrectCarNumber as exc:
            print(exc.message, exc.data)
            return False


class IncorrectVinNumber(Exception):
    def __init__(self, message='Incorrect VIN', data=''):
        self.message = message
        self.data = data


class IncorrectCarNumber(Exception):
    def __init__(self, message='Incorrect Car number', data=''):
        self.message = message
        self.data = data


first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 2020202, 'нет номера')