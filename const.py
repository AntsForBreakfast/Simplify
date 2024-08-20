from termcolor import colored

from schemas import TermColor, TermHighlight, ColorPalettes

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

TEXT_LENGTH: int = 92
TEXT_COLOR: TermColor = "black"
TEXT_HIGHLIGHTS: dict[str, TermHighlight] = {
    "header": "on_blue",
    "phonetic": "on_green",
    "part_of_speech": "on_yellow",
    "definition": "on_magenta",
    "example": "on_red",
    "number": "on_cyan",
    "multiline_separator": "on_cyan",
}
COLOR_PALETTES: ColorPalettes = {
    k: (TEXT_COLOR, v) for k, v in TEXT_HIGHLIGHTS.items()
}

MULTILINE_MARK: str = " |  "
COLORED_MUTILINE_MARK: str = colored(
    MULTILINE_MARK, TEXT_COLOR, TEXT_HIGHLIGHTS["multiline_separator"]
)
