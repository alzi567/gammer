"""Main module."""

import logging
from pathlib import Path

import click

from gammer.gam import Gam
from gammer.generate import generate_something, image_to_cubes
from gammer.image import get_pixel_matrix

logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.argument("image", type=click.Path(exists=True, dir_okay=False))
@click.argument("output", type=click.Path(exists=False, dir_okay=False))
def cli(image: Path, output: Path):
    """Main function.

    Either the entrance point of the command line interface or a simple example
    on how to use this package.
    """
    pixels = get_pixel_matrix(image_path=image)
    objects = image_to_cubes(pixels=pixels)

    # objects = generate_something()
    gam = Gam()
    gam.write(filename=Path(output), objects=objects)


if __name__ == "__main__":
    cli()
