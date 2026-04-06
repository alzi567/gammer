"""Tests for the multiplication feature."""


from gammer.multiply import multiply


def test_multiply():
    """Test standard case: multiply two numbers."""
    result = multiply(3, 7)
    assert result == 21
