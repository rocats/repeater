import json
from typing import Any, List
from pyaml_env import parse_config
from urllib.request import urlopen

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


def load_library(url: str) -> List[str]:
    data = json.loads(urlopen(url).read().decode("utf-8"))["rows"]
    return [item[2] for item in data]


# load libraries
sticker_lib = load_library(
    "https://repeater-bot-sqlite.vercel.app/remote/stickers.json"
)
char_lib = load_library("https://repeater-bot-sqlite.vercel.app/remote/words.json")
animation_lib = load_library(
    "https://repeater-bot-sqlite.vercel.app/remote/animations.json"
)
