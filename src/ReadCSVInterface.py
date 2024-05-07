import abc


class ReadCSVInterface(abc.ABC):

    @abc.abstractmethod
    def get_file_data(self, filename):
        pass