from urllib.parse import urljoin

from requests import get

from color import color_output
from commands import command_parser
from const import COLOR_PALETTES, URL
from word_dictionary import get_dictionary, render_dictionary

args = command_parser()

print(args)
if not any(map(str.isdigit, args.word)):

    url = urljoin(URL, args.word)
    response = get(url)

    if response.status_code == 200:
        info = get_dictionary(response)
        colored = color_output(word_info=info, palettes=COLOR_PALETTES)
        render_dictionary(colored, args.lines)
    else:
        print("Request didint go through")
else:
    print("Command argument: 'word' - contains digits")
