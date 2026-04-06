"""Generate a wonderful GAM scenery."""

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


def image_to_cubes(pixels) -> list[GamObject]:
    """Convert image pixels to GamCubes.

    Args:
        pixels (_type_): _description_

    Returns:
        list[GamObject]: _description_
    """
    objects = []
    grid = 1.1
    for y, row in enumerate(pixels):
        for x, col in enumerate(row):
            objects.append(
                GamCube(
                    x=x * grid,
                    y=y * grid,
                    z=0,
                    side_length=1,
                    color=GamColor(r=col[0], g=col[1], b=col[2]),
                )
            )
    return objects
