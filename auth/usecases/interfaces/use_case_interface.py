import abc


class UseCaseInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self):
        pass
