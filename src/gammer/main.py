"""Main module."""
import logging
from argparse import ArgumentParser

from rich.logging import RichHandler

from .multiply import multiply

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET",
    format=FORMAT,
    handlers=[RichHandler(rich_tracebacks=True)],
)

logging.basicConfig(level=logging.DEBUG)

# first number to be multiplied
FIRST_NUMBER = 3


def parse_args():
    """Parse command-line args."""
    parser = ArgumentParser(
        prog="gammer",
        description="Python skeleton app. Will multiply 3 with another value.",
    )

    parser.add_argument(
        "--multiplicator",
        "-m",
        type=int,
        help="set the multiplicator",
        default=5,
    )

    return parser.parse_args()


def main():
    """Main function.

    Either the entrance point of the command line interface or a simple example
    on how to use this package.
    """
    args = parse_args()

    result = multiply(FIRST_NUMBER, args.multiplicator)
    logging.info("The result of %s x %s = %s", FIRST_NUMBER, args.multiplicator, result)
