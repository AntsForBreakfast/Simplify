import argparse

from schemas import Namespace


def command_parser() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="Simplify",
        description="Gives information about the word",
    )

    parser.add_argument("word", help="Single word")
    parser.add_argument("-l", "--lines", type=int, help="Definitions lines")

    return parser.parse_args()
