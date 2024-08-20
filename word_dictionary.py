from requests.models import Response

from const import COLORED_MUTILINE_MARK, TEXT_LENGTH
from schemas import WordInfo
from string_mod import multiline_text


def get_dictionary(response: Response) -> WordInfo:
    """Gives back a dictionary with information about the word

    response: request.models.Response
    returns: WordInfo
    """
    data = response.json()[0]

    header = f" {data["word"].capitalize()} "
    phonetic = f" {data.get('phonetic', '')}"
    meanings = data["meanings"][0]
    part_of_speech = f" {meanings["partOfSpeech"].capitalize()} "

    definitions = []
    for n, d in enumerate(meanings["definitions"], 1):
        td = {}

        # String lenght 4 and numbers allign to the right
        td["number"] = f" {str(n).ljust(3, ' ')}"

        for k, v in d.items():
            if not v:
                continue

            # Multiline text
            mt = multiline_text(f" {v}", TEXT_LENGTH)

            # Separate multiline text into each line
            # Fill the line with empty spaces
            td[k] = [f"{t.ljust(TEXT_LENGTH, ' ')}\n" for t in mt.split("\n")]

        definitions.append(td)

    return {
        "header": header,
        "phonetic": phonetic,
        "part_of_speech": part_of_speech,
        "definitions": definitions,
    }


def render_dictionary(word_info: WordInfo, lines: int) -> None:
    print(word_info["header"] + word_info["phonetic"] + word_info["part_of_speech"])

    text = ""
    for word_def in word_info["definitions"][:lines]:
        number = word_def["number"]
        definition = word_def["definition"]
        example = word_def.get("example", "")

        for n, d in enumerate(definition):
            text += number if n == 0 else COLORED_MUTILINE_MARK
            text += d

        if isinstance(example, list):
            for n, e in enumerate(example):
                text += COLORED_MUTILINE_MARK + e
        else:
            text += COLORED_MUTILINE_MARK + "".join(example)

    print(text)
