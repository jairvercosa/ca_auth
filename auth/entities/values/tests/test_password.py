import pytest

from auth.entities.values.password import Password


class TestInit:

    def test_set_value_without_encryption(self):
        password = Password('password')
        assert password.value == 'password'

    def test_when_password_is_not_passed_in_set_value_none(self):
        password = Password(None)
        assert password.value is None


class TestPasswordValueSetter:

    def test_when_password_is_not_strong_raises_password_strength_error(self):
        with pytest.raises(ValueError):
            password_value = Password(None)
            password_value.value = 'pass'

    def test_when_password_is_strong_stores_it_encrypted(self):
        password = 'P@ssword9'
        password_value = Password(None)
        password_value.value = password

        assert password_value.value != password


class TestValidateStrength:

    def test_when_password_is_none_returns_false(self):
        result, _ = Password.validate_strength(None)
        assert result is False

    def test_when_password_length_less_than_8_returns_legth_false_on_the_dict(self):
        _, result = Password.validate_strength('pass')
        assert result.get('length') is False

    def test_when_password_length_greather_than_7_returns_legth_true_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('length') is True

    def test_when_password_has_no_digit_returns_digit_false_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('digit') is False

    def test_when_password_has_a_digit_returns_digit_true_on_the_dict(self):
        _, result = Password.validate_strength('password9')
        assert result.get('digit') is True

    def test_when_password_has_no_uppercase_returns_uppercase_false_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('uppercase') is False

    def test_when_password_has_an_uppercase_returns_uppercase_true_on_the_dict(self):
        _, result = Password.validate_strength('passworD')
        assert result.get('uppercase') is True

    def test_when_password_has_no_lowercase_returns_lowercase_false_on_the_dict(self):
        _, result = Password.validate_strength('PASSWORD')
        assert result.get('lowercase') is False

    def test_when_password_has_a_lowercase_returns_lowercase_true_on_the_dict(self):
        _, result = Password.validate_strength('PASSWORd')
        assert result.get('lowercase') is True

    def test_when_password_has_no_symbols_returns_symbol_false_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('symbol') is False

    def test_when_password_has_a_symbols_returns_symbol_true_on_the_dict(self):
        _, result = Password.validate_strength('p@ssword')
        assert result.get('symbol') is True

    def test_when_password_length_less_than_8_returns_false(self):
        result, _  = Password.validate_strength('pass')
        assert result is False

    def test_when_password_has_no_digit_returns_false(self):
        result, _  = Password.validate_strength('password')
        assert result is False

    def test_when_password_has_no_uppercase_returns_false(self):
        result, _  = Password.validate_strength('password9')
        assert result is False

    def test_when_password_has_no_lowercase_returns_false(self):
        result, _  = Password.validate_strength('PASSWORD9')
        assert result is False

    def test_when_password_has_no_symbols_returns_false(self):
        result, _  = Password.validate_strength('passworD9')
        assert result is False

    def test_when_password_is_strong_returns_true(self):
        result, _  = Password.validate_strength('p@ssworD9')
        assert result is True


class TestEq:

    def test_when_value_is_different_from_original_password_value_returns_false(self):
        pass_a = Password(None)
        pass_a.value = 'P@ssword9'

        assert bool(pass_a == 'p@ssword9') is False

    def test_when_value_is_equal_from_original_password_value_returns_true(self):
        original_password = 'P@ssword9'
        pass_a = Password(None)
        pass_a.value = original_password

        assert bool(pass_a == original_password) is True


class TestReq:

    def test_has_encrypted_value(self):
        pass_a = Password(None)
        pass_a.value = 'P@ssword9'

        assert pass_a.value in str(pass_a)
