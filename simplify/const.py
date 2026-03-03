from rich.color import Color, ColorType
from rich.color_triplet import ColorTriplet
from rich.style import Style

from .schemas import StyleParams, TextBgColor, TextColor

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

# Number and multiline mark size. Ps. rip name
SIDE_PANNEL_LENGTH: int = 4

COLOR_TYPE: ColorType = ColorType.TRUECOLOR

WI_TRIPLETS: dict[str, tuple[TextColor, TextBgColor]] = {
    "header": (ColorTriplet(0, 0, 0), ColorTriplet(0, 64, 255)),
    "phonetic": (ColorTriplet(0, 0, 0), ColorTriplet(0, 122, 0)),
    "part_of_speech": (ColorTriplet(0, 0, 0), ColorTriplet(255, 255, 0)),
    "definition": (ColorTriplet(0, 0, 0), ColorTriplet(204, 51, 153)),
    "example": (ColorTriplet(0, 0, 0), ColorTriplet(50, 100, 50)),
    "number": (ColorTriplet(0, 0, 0), ColorTriplet(204, 255, 255)),
    "multiline_mark": (ColorTriplet(0, 0, 0), ColorTriplet(0, 210, 255)),
}

WI_COLORS: dict[str, tuple[Color, Color]] = {
    k: (
        Color(name=f"text-{k}", type=COLOR_TYPE, triplet=rgb[0]),
        Color(name=f"bg-{k}", type=COLOR_TYPE, triplet=rgb[1]),
    )
    for k, rgb in WI_TRIPLETS.items()
}

# Yes, redundant, deal with it
STYLE_PARAMS: dict[str, StyleParams] = {
    "header": {
        "color": WI_COLORS["header"][0],
        "bgcolor": WI_COLORS["header"][1],
    },
    "phonetic": {
        "color": WI_COLORS["phonetic"][0],
        "bgcolor": WI_COLORS["phonetic"][1],
    },
    "part_of_speech": {
        "color": WI_COLORS["part_of_speech"][0],
        "bgcolor": WI_COLORS["part_of_speech"][1],
    },
    "definition": {
        "color": WI_COLORS["definition"][0],
        "bgcolor": WI_COLORS["definition"][1],
    },
    "example": {
        "color": WI_COLORS["example"][0],
        "bgcolor": WI_COLORS["example"][1],
    },
    "number": {
        "color": WI_COLORS["number"][0],
        "bgcolor": WI_COLORS["number"][1],
    },
    "multiline_mark": {
        "color": WI_COLORS["multiline_mark"][0],
        "bgcolor": WI_COLORS["multiline_mark"][1],
    },
}

WI_STYLES = {k: Style(**v) for k, v in STYLE_PARAMS.items()}

