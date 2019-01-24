import re

from ..encryptor import Encryptor


class Password:

    def __init__(self, value: str):
        self.__value = value

    def __bool__(self):
        return bool(self.__value)

    def __eq__(self, value):
        return Encryptor.verify(value, self.__value)

    def __repr__(self):
        return '< Password object {}>'.format(self.__value)

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        valid_password, _ = self.validate_strength(value)
        if not valid_password:
            raise ValueError(
                'A strong password should contain at least 8 characters, '
                '1 digit, 1 symbol, 1 uppercase letter, and 1 lowercase '
                'letter'
            )

        self.__value = Encryptor.encrypt(value)

    @classmethod
    def validate_strength(cls, value: str) -> (bool, dict):
        """
        Verify the strength of 'password', it returns a dict with
        bool values for each validation.

        A password is considered strong if:
            8 characters length or more
            1 digit or more
            1 symbol or more
            1 uppercase letter or more
            1 lowercase letter or more
        """
        if value is None:
            return False, {}

        length = cls._validate_length(value)
        digit = cls._validate_digit(value)
        uppercase = cls._validate_uppercase(value)
        lowercase = cls._validate_lowercase(value)
        symbol = cls._validate_symbol(value)

        valid = all([length, digit, uppercase, lowercase, symbol])
        error_dict = {
            'length': length,
            'digit': digit,
            'uppercase': uppercase,
            'lowercase': lowercase,
            'symbol': symbol,
        }

        return valid, error_dict

    @classmethod
    def _validate_length(cls, value: str) -> bool:
        return not len(value) < 8

    @classmethod
    def _validate_digit(cls, value: str) -> bool:
        return bool(re.search(r"\d", value))

    @classmethod
    def _validate_uppercase(cls, value: str) -> bool:
        return bool(re.search(r"[A-Z]", value))

    @classmethod
    def _validate_lowercase(cls, value: str) -> bool:
        return bool(re.search(r"[a-z]", value))

    @classmethod
    def _validate_symbol(cls, value: str) -> bool:
        return bool(re.search(r"\W", value))
