from termcolor import colored

from const import TEXT_LENGTH
from schemas import ColorPalettes, WordInfo


def color_output(word_info: WordInfo, palettes: ColorPalettes) -> WordInfo:
    # Colors everything besides definitions
    for k, v in word_info.items():
        if k != "definitions":
            word_info[k] = colored(v, *palettes[k])

    # Colors only definitions
    for definition in word_info["definitions"]:
        if isinstance(definition, dict):
            for k, v in definition.items():
                if isinstance(v, list) and k in ("definition", "example"):
                    definition[k] = [colored(s, *palettes[k]) for s in v]
                elif k == "number":
                    definition[k] = colored(v, *palettes[k])

            # Create empty example if not present
            # Acts like line separator between definition

            if "example" not in definition:
                definition["example"] = colored(
                    " " * TEXT_LENGTH + "\n", *palettes["example"]
                )

    return word_info
