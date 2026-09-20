#!/usr/bin/env python3
"""Shrink every image in a folder in place to max 2000px on the long edge (needs: pip install pillow).
Usage: python3 tools/resize.py 2026-10-sengupta-family-singapore/photos
"""
import os, sys
from PIL import Image, ImageOps
folder = sys.argv[1]
for f in os.listdir(folder):
    p = os.path.join(folder, f)
    if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue
    im = ImageOps.exif_transpose(Image.open(p))
    im.thumbnail((2000, 2000))
    im.convert('RGB').save(os.path.splitext(p)[0] + '.jpg', quality=85, optimize=True)
    if not f.lower().endswith(('.jpg', '.jpeg')):
        os.remove(p)
print('done')
