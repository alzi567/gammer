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
    for i in range(1, 10):
        objects.append(  # noqa: PERF401
            GamCube(x=i * grid, y=0, z=0, side_length=1, color=GamColor(r=i * 20, g=i * 20, b=0)),
        )

    return objects
