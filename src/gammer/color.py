"""Color object."""


class GamColor:
    """Color object."""

    def __init__(self, r: int, g: int, b: int) -> None:
        """Initialize."""
        self.r = r
        self.g = g
        self.b = b

    def render(self) -> str:
        """Render the color in GAM syntax.

        Returns:
            str: _description_
        """
        color = int(self.b << 16) + int(self.g << 8) + int(self.r)
        return f"{color:d}"
