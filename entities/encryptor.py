from passlib.hash import argon2

from .interfaces import EncryptorInterface


class Encryptor(EncryptorInterface):
    __salt = "492MIj$M"

    @classmethod
    def encrypt(cls, value):
        if isinstance(value, str):
            salt = str.encode(cls.__salt)
            return argon2.using(rounds=4, salt=salt).hash(value)

        raise ValueError('The value to encrypt must to be a string.')

    @classmethod
    def verify(cls, value, encrypted):
        return argon2.verify(value, encrypted)
