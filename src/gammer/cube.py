"""Cube object."""

from gammer.color import GamColor


class GamCube:
    """Cube object."""

    def __init__(self, x: float, y: float, z: float, side_length: float, color: GamColor) -> None:
        """Initialize."""
        self.x = x
        self.y = y
        self.z = z
        self.side_length = side_length
        self.color = color

    def render(self) -> str:
        """Render the cube in GAM syntax.

        Returns:
            str: _description_
        """
        return (
            f"EW {self.color.render()},1\n"
            f"  T({self.x},{self.y},{self.z})\n"
            f"  S({self.side_length},{self.side_length},{self.side_length})\n"
        )
