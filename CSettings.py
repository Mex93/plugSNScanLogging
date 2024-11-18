import re


class Settings:
    current_model = ""
    current_vender = ""
    current_lot_count = 0
    current_sns = 0

    # getters
    @classmethod
    def get_model(cls) -> str:
        return cls.current_model

    @classmethod
    def get_vender(cls) -> str:
        return cls.current_vender

    @classmethod
    def get_lot_count(cls) -> int:
        return cls.current_lot_count

    @classmethod
    def get_sns(cls) -> int:
        return cls.current_sns

    # setters
    @classmethod
    def set_model(cls, name: str) -> None:
        cls.current_model = name

    @classmethod
    def set_vender(cls, name: str) -> None:
        cls.current_vender = name

    @classmethod
    def set_lot_count(cls, count: str | int) -> None:
        cls.current_lot_count = cls.convert_data_to_int(count)

    @classmethod
    def set_sns(cls, count: str | int) -> None:
        cls.current_sns = cls.convert_data_to_int(count)

    @classmethod
    def convert_data_to_int(cls, count: str | int) -> int:
        if isinstance(count, int):
            return count
        elif isinstance(count, str):
            try:
                return int(count)
            except:
                return -1

    @classmethod
    def is_vendor_valid(cls, string: str) -> bool:
        if isinstance(string, str):
            if 3 <= len(string) <= 32:
                if cls.is_only_latin_and_sym(string):
                    return True
        return False

    @classmethod
    def is_model_valid(cls, string: str) -> bool:
        if isinstance(string, str):
            if 3 <= len(string) <= 64:
                if cls.is_model_sym_valid(string):
                    return True
        return False

    @classmethod
    def is_model_sym_valid(cls, text):
        pattern = r'^[A-Za-z0-9а-яА-Я \-.|/|\\]+$'
        return re.match(pattern, text)

    @classmethod
    def is_only_latin_and_sym(cls, text):
        pattern = r'^[A-Za-z0-9 \-.|/|\\]+$'
        return re.match(pattern, text)

    @classmethod
    def is_valid_sn(cls, text):
        pattern = r'^[A-Za-z0-9*\-]+$'
        return re.match(pattern, text)

    @classmethod
    def is_only_integer(cls, text):
        pattern = r'^[0-9]+$'
        return re.match(pattern, text)
