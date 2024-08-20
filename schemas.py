from argparse import Namespace
from typing import TypedDict
from termcolor._types import Color, Highlight

type TermColor = Color
type TermHighlight = Highlight
type ColorPalettes = dict[str, tuple[TermColor, TermHighlight]]


class WordDefinition(TypedDict):
    definition: list[str]
    example: list[str]
    number: str


class WordInfo(TypedDict):
    header: str
    part_of_speech: str
    phonetic: str
    definitions: list[WordDefinition]
