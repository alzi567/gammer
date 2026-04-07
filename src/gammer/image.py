"""Extract pixels from an image."""

import re
from math import floor, sqrt
from pathlib import Path

import numpy as np
from PIL import Image, ImageOps


def get_dimensions(width: int, height: int, pixels: int) -> tuple[int, int]:
    """From a maximum number of pixels, calculate the reduced width and height, preserving the aspect ratio.

    Args:
        width (int): the original width of the image
        height (int): the original height of the image
        pixels (int): the maximum number of pixels in the reduced image

    Returns:
        tuple[int, int]: width and height of the reduced image, having the same aspect ration and the specified
            maximum number of pixels
    """
    aspect_ratio = height / width

    # height = aspect_ratio * width

    # pixels = width * height = width * aspect_ratio * width
    reduced_width = floor(sqrt(pixels / aspect_ratio))
    reduced_height = floor(reduced_width * aspect_ratio)

    return reduced_width, reduced_height


def parse_limit(size: str) -> tuple[int, int]:
    """Parse the limit string into a tuple of (x, y).

    Args:
        size (str): size string in the format XxY, e.g. '30x40'

    Returns:
        tuple[int,int]: the tuple of (max_x, max_y)
    """
    pattern = r"^\d+x\d+$"

    if not re.match(pattern, size):
        msg = f"wrong format in 'size' option. Expected something like '20x10', but found: '{size}'"
        raise ValueError(msg)

    x, y = size.split("x")
    return int(x), int(y)


def get_pixel_matrix(image_path: Path, bw: bool, limit: str | None = None, max_pixels: int | None = None) -> None:
    """Extract pixel matrix from an image file.

    Args:
        image_path (Path): Der Pfad zur JPG-Datei.
        limit (str | None, optional): restrict GAM output to a maximum number of x and y pixels.
            Format:
                * either: XxY, e.g. '40x30'. Aspect ratio will be preserved. Defaults to None.
                * or: XXpx, e.g. '500px'. Specifies the maximum number of pixels of the downscaled image.
        max_pixels (int | None, optional): restrict GAM output to this maximum number of total pixels.

    Returns:
        numpy.ndarray: Eine 3D-NumPy-Array, das die Pixelmatrix darstellt,
            oder None, wenn ein Fehler auftritt.
            Das Array hat die Form (Höhe, Breite, Kanäle),
            wobei Kanäle (Rot, Grün, Blau) sind.
    """
    try:
        # 1. Das Bild öffnen
        img = Image.open(image_path)
        print(f"Bild erfolgreich geöffnet: {image_path}")
        print(f"Bildformat: {img.format}")
        print(f"Bildmodus: {img.mode}")  # Z.B. 'RGB' für Farbbilder, 'L' für Graustufen
        print(f"Originale Bildgröße: {img.size} (Breite x Höhe)")

        # size give => restrict image to the given size, if it is bigger
        img_width, img_height = img.size

        if max_pixels:
            max_width1, max_height1 = get_dimensions(width=img_width, height=img_height, pixels=max_pixels)
            if img_width > max_width1 or img_height > max_height1:
                img.thumbnail((max_width1, max_height1))
                new_x, new_y = img.size
                print(f"Heruntergerechnete Bildgröße: {img.size} (Breite x Höhe) = {new_x * new_y} pixels.")

        if limit:
            max_width2, max_height2 = parse_limit(limit)
            if img_width > max_width2 or img_height > max_height2:
                img.thumbnail((max_width2, max_height2))
                new_x, new_y = img.size
                print(f"Heruntergerechnete Bildgröße: {img.size} (Breite x Höhe) = {new_x * new_y} pixels.")

        if bw:
            # make grayscale image
            img = ImageOps.grayscale(img)
            print("Umgewandelt auf Graustufen.")

        # 2. Das Bild in ein NumPy-Array umwandeln
        # Dies ist die gängigste Methode, um die Pixelmatrix zu erhalten.
        # Das resultierende Array hat die Form (Höhe, Breite, Kanäle).
        pixel_matrix = np.array(img)

        print(f"Form der Pixelmatrix: {pixel_matrix.shape}")
        print(f"Datentyp der Pixelmatrix: {pixel_matrix.dtype}")

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{image_path}' wurde nicht gefunden.")
        return None
    else:
        return pixel_matrix


# --- Beispielanwendung ---
if __name__ == "__main__":
    # Erstelle eine Dummy-JPG-Datei für Testzwecke
    try:
        from PIL import Image, ImageDraw

        # Erstelle ein kleines, farbiges Bild
        dummy_img = Image.new("RGB", (10, 5), color="red")  # 10x5 rotes Bild
        draw = ImageDraw.Draw(dummy_img)
        draw.rectangle((2, 1, 7, 3), fill="blue")  # Ein blaues Rechteck einzeichnen
        dummy_image_path = "test_image.jpg"
        dummy_img.save(dummy_image_path)
        print(f"Dummy-Bild '{dummy_image_path}' für Testzwecke erstellt.")
    except Exception as e:
        print(f"Konnte Dummy-Bild nicht erstellen: {e}")
        dummy_image_path = "path/to/your/image.jpg"  # Bitte hier deinen Bildpfad anpassen

    # Pfad zu deiner JPG-Datei
    # dummy_image_path = "path/to/your/image.jpg" # Wenn du kein Dummy-Bild erstellen möchtest, kommentiere die obigen Zeilen aus und nutze diese.

    pixel_data = get_pixel_matrix(dummy_image_path)

    if pixel_data is not None:
        print("\nErste 5 Zeilen und Spalten der Pixelmatrix (RGB-Werte):")
        # Zeigt die ersten paar Pixelwerte an, um einen Eindruck zu bekommen
        # Beachte, dass dies nur ein kleiner Ausschnitt ist, die gesamte Matrix kann sehr groß sein!
        print(pixel_data[:5, :5, :])
        print(f"\nDer Pixel an Position (0,0) hat die RGB-Werte: {pixel_data[0, 0]}")
        print(f"Der Pixel an Position (2,2) hat die RGB-Werte: {pixel_data[2, 2]}")  # Sollte blau sein (0,0,255)
    else:
        print("Konnte die Pixelmatrix nicht extrahieren.")
