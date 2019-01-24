import pytest

from entities import Encryptor


class TestEncrypt:

    def test_return_a_string(self):
        result = Encryptor.encrypt('Password')
        assert isinstance(result, str)

    def test_when_value_is_not_string_raise_exception(self):
        with pytest.raises(ValueError):
            Encryptor.encrypt(123)

    def test_return_encrypted_value(self):
        expected_value = '$argon2i$v=19$m=102400,t=4,p=8$NDkyTUlqJE0$K4PWIcRV17QtJn++dv4YqA'
        assert Encryptor.encrypt('pass') == expected_value


class TestVerify:

    def test_when_values_mismatch_return_false(self):
        encrypted = '$argon2i$v=19$m=102400,t=4,p=8$NDkyTUlqJE0$K4PWIcRV17QtJn++dv4YqA'
        assert Encryptor.verify('test', encrypted) is False

    def test_when_values_match_return_true(self):
        value = 'pass'
        encrypted = Encryptor.encrypt(value)
        assert Encryptor.verify(value, encrypted) is True
