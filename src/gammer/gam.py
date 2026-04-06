"""GAM file generator."""

from pathlib import Path


class Gam:
    """GAM file handler."""

    def __init__(self) -> None:
        """Initialize."""

    def render(self, objects: list) -> str:
        """Render the GAM objects into a GAM file syntax string.

        The result is ready to be written to a GAM project file.

        Args:
            objects (list): the GAM objects to be written
        """
        result = [obj.render() for obj in objects]

        return "\n".join(result)

    def write(self, objects: list, filename: Path) -> None:
        """Write a file.

        Args:
            objects (list): the GAM objects to be written
            filename (Path): _description_
        """
        content = self.render(objects)
        filename.write_text(content)
