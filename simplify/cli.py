from urllib.parse import urljoin

from requests import get
from rich.console import Console

from .commands import command_parser
from .const import URL
from .word_dictionary import add_styles, get_word_info, render

def main():
    args = command_parser()
    terminal = Console()

    if not any(map(str.isdigit, args.word)):

        url = urljoin(URL, args.word)
        response = get(url)

        if response.status_code == 200:
            info = get_word_info(response)
            style_info = add_styles(info)
            render(terminal, style_info, args.lines)
        else:
            print("Request didint go through")
    else:
        print("Command argument: 'word' - contains digits")
