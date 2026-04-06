"""Extract pixels from an image."""

from pathlib import Path

import numpy as np
from PIL import Image


def get_pixel_matrix(image_path: Path) -> None:
    """Extrahiert die Pixelmatrix aus einer JPG-Datei.

    Args:
        image_path (Path): Der Pfad zur JPG-Datei.

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
        print(f"Bildgröße: {img.size} (Breite x Höhe)")

        # 2. Das Bild in ein NumPy-Array umwandeln
        # Dies ist die gängigste Methode, um die Pixelmatrix zu erhalten.
        # Das resultierende Array hat die Form (Höhe, Breite, Kanäle).
        pixel_matrix = np.array(img)

        print(f"Form der Pixelmatrix: {pixel_matrix.shape}")
        print(f"Datentyp der Pixelmatrix: {pixel_matrix.dtype}")

        return pixel_matrix

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{image_path}' wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None


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
