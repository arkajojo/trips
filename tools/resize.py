#!/usr/bin/env python3
"""Shrink every image in a folder in place to max 2000px on the long edge (pip install pillow).
Usage: python3 tools/resize.py arka/2026-10-treena-swapnadeep-ayanshi/photos
"""
import os, sys
from PIL import Image, ImageOps
folder = sys.argv[1]
for f in os.listdir(folder):
    p = os.path.join(folder, f)
    if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): continue
    im = ImageOps.exif_transpose(Image.open(p)); exif = im.info.get('exif')
    im.thumbnail((2000, 2000))
    out = os.path.splitext(p)[0] + '.jpg'
    im.convert('RGB').save(out, quality=85, optimize=True, **({'exif': exif} if exif else {}))
    if out != p: os.remove(p)
print('done')
