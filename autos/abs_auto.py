import abc


class AbsAuto(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    def __str__(self):
        return self.__class__.__name__