from patterns_example.proxy.txt_reader import TxtReader
from patterns_example.proxy.txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result, self.__is_actual

    def write_file(self, new_text):
        if self.__result == new_text:
            return self.__result
        else:
            self.__result = self.__txt_writer.write(new_text)
            self.__is_actual = False
            return self.__result



