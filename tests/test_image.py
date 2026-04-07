"""Tests for the multiplication feature."""

import pytest

from gammer.image import get_dimensions


@pytest.mark.parametrize(
    ("width", "height", "pixels", "width2", "height2"),
    [
        (1000, 500, 50, 10, 5),
        (1000, 500, 49, 9, 4),
    ],
)
def test_get_dimensions(width: int, height: int, pixels: int, width2: int, height2: int):
    """Test standard case: multiply two numbers."""
    assert get_dimensions(width=width, height=height, pixels=pixels) == (width2, height2)
