"""Generate a wonderful GAM scenery."""

import numpy as np

from gammer.color import GamColor
from gammer.cube import GamCube
from gammer.object import GamObject


def generate_something() -> list[GamObject]:
    """Generate a GAN project.

    Returns:
        list[GamObject]: _description_
    """
    objects = []
    grid = 1.1
    size = 60
    for y in range(size):
        for x in range(size):
            objects.append(  # noqa: PERF401
                GamCube(
                    x=x * grid,
                    y=y * grid,
                    z=0,
                    side_length=1,
                    color=GamColor(r=x * (255 // size), g=y * (255 // size), b=0),
                ),
            )

    return objects


def image_to_cubes(pixels, margin: float = 0) -> list[GamObject]:
    """Convert image pixels to GamCubes.

    Args:
        pixels (_type_): _description_

    Returns:
        list[GamObject]: _description_
    """
    objects = []
    grid = 1.0 + margin
    for y, row in enumerate(pixels):
        for x, col in enumerate(row):
            if np.isscalar(col):
                color = GamColor(r=int(col), g=int(col), b=int(col))
            else:
                color = GamColor(r=int(col[0]), g=int(col[1]), b=int(col[2]))
            objects.append(
                GamCube(
                    x=y * grid,
                    y=x * grid,
                    z=0,
                    side_length=1,
                    color=color,
                )
            )
    return objects
