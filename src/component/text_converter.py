import opencc


class TextConverter:
    """text converter functional class with OpenCC"""

    def __init__(self) -> None:
        self.modes = ["t2s", "s2t"]
        self.current_mode = "t2s"
        self.is_traditional = False

    def select_mode(self, mode: str) -> None:
        self.current_mode = mode

    def check_traditional(self, text: str) -> bool:
        converter = opencc.OpenCC("t2s.json")
        if converter.convert(text) != text:
            self.is_traditional = True
        return self.is_traditional

    def convert(self, text: str) -> str:
        converter = opencc.OpenCC(f"{self.current_mode}.json")
        return converter.convert(text)


tc = TextConverter()
