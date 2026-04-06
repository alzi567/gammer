"""Main module."""

import logging
from pathlib import Path

import click

from gammer.gam import Gam
from gammer.generate import generate_something

logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.argument("output", type=click.Path(exists=False, dir_okay=False))
def cli(output: Path):
    """Main function.

    Either the entrance point of the command line interface or a simple example
    on how to use this package.
    """
    objects = generate_something()
    gam = Gam()
    gam.write(filename=Path(output), objects=objects)


if __name__ == "__main__":
    cli()
