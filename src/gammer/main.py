"""Main module."""

import logging
from pathlib import Path

import click

from gammer.gam import Gam
from gammer.generate import generate_something, image_to_cubes
from gammer.image import get_pixel_matrix

logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.option(
    "--margin",
    type=float,
    default=0.0,
    help=("gutter between the cubes. 0 means no gutter, 1 means a space of one cube size between each cubes."),
)
@click.argument("image", type=click.Path(exists=True, dir_okay=False))
@click.argument("output", type=click.Path(exists=False, dir_okay=False))
def cli(image: Path, output: Path, margin: float):
    """Extract pixels from the given image file and render a GAM file representing this image.

    The first argument [image] is the filename of the image input file (JPG). The second argument [output] is the
    GAM output file which will be generated.
    """
    pixels = get_pixel_matrix(image_path=image)
    objects = image_to_cubes(pixels=pixels, margin=margin)

    # objects = generate_something()
    gam = Gam()
    gam.write(filename=Path(output), objects=objects)


if __name__ == "__main__":
    cli()
