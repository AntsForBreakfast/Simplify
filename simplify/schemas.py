from argparse import Namespace
from typing import TypedDict

from rich.color import Color
from rich.color_triplet import ColorTriplet
from rich.text import Text

type TextColor = ColorTriplet
type TextBgColor = ColorTriplet


class WordInfo(TypedDict):
    header: Text 
    part_of_speech: Text 
    phonetic: Text 
    definitions: list[dict[str, Text]]


class StyleParams(TypedDict):
    color: Color
    bgcolor: Color
