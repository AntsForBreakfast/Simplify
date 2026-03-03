from requests.models import Response
from rich.console import Console
from rich.containers import Lines
from rich.text import Text

from .const import SIDE_PANNEL_LENGTH, WI_STYLES
from .schemas import WordInfo


def get_word_info(response: Response) -> WordInfo:
    """Gives back a dictionary with information about the word

    response: request.models.Response
    returns: WordInfo
    """
    data = response.json()[0]
    meanings = data["meanings"][0]

    header = Text(text=data["word"].capitalize())
    phonetic = Text(text=data.get("phonetic", ""))
    part_of_speech = Text(text=meanings["partOfSpeech"].capitalize())
    definitions = [
        {
            "definition": Text(text=" " + dd.get("definition", "")),
            "example": Text(text=" " + dd.get("example", ""), end=""),
            "number": Text(text=str(n).center(4, " "), end=""),
            "multiline_mark": Text(text="|".center(4, " "), end=""),
        }
        for n, dd in enumerate(meanings["definitions"], 1)
    ]

    return {
        "header": header,
        "phonetic": phonetic,
        "part_of_speech": part_of_speech,
        "definitions": definitions,
    }


def add_styles(word_info: WordInfo) -> WordInfo:
    for k, v in word_info.items():
        if k != "definitions" and isinstance(v, Text):
            v.stylize(style=WI_STYLES[k])

    for wi in word_info["definitions"]:
        for k, v in wi.items():
            if isinstance(v, Text):
                v.stylize(style=WI_STYLES[k])

    return word_info


def render(terminal: Console, word_info: WordInfo, definition_count: int=0):
    if definition_count == 0:
       definition_count = len(word_info['definitions'])

    for wi in word_info["definitions"][:definition_count]:
        text = Text(text='')
        for k in "definition", "example":

            # Separate text into different lines
            lines: Lines = wi[k].wrap(
                console=terminal,
                width=terminal.width - SIDE_PANNEL_LENGTH - 1,
            )

            if k == 'definition':
                text.append(wi["number"])
            else:
                text.append('\n')
                text.append_text(wi["multiline_mark"])

            lines[0].extend_style(terminal.width - SIDE_PANNEL_LENGTH)
            text.append_text(lines[0])

            # Appending text
            for line in lines[1:]:
                text.append('\n')
                text.append_text(wi["multiline_mark"])
                text.append(' ', style=WI_STYLES[k])

                line.extend_style(terminal.width - SIDE_PANNEL_LENGTH)
                text.append_text(line)

        terminal.print(text)
