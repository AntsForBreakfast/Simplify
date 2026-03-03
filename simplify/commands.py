import argparse

from .schemas import Namespace


def command_parser() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="Simplify",
        description="Gives information about the word",
    )

    parser.add_argument("word", help="Single word")
    parser.add_argument("-l", "--lines", type=int, help="Definitions lines")
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")

    return parser.parse_args()
