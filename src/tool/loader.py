from typing import Any
from pyaml_env import parse_config

from model.config import AppConfig

"""config loader"""


class Parser:
    def __init__(self, dic: dict) -> None:
        self.dic: dict = dic

        def recursive_check(obj) -> None:
            for key, value in dic.items():
                if isinstance(value, dict):
                    value = Parser(value)
                setattr(obj, key, value)

        recursive_check(self)

    def get_attr(self):
        return AppConfig(
            debug=self.dic["app"]["debug"],
            env=self.dic["app"]["env"],
            log_level=self.dic["app"]["log_level"],
        )


def load_config() -> Any:
    return Parser(parse_config("config.yaml")).get_attr()
