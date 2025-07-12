import os
import sys

import cairosvg
from PIL import Image
from io import BytesIO

path = sys.argv[1]
with open(path, "r") as f:
    svg_content = f.read()
img_png = cairosvg.svg2png(svg_content)
img = Image.open(BytesIO(img_png))
name, ext = os.path.splitext(path)
img.save(f"{name}.png")