#!/usr/bin/env python3
"""Rebuild <trip>/photos/photos.json from the images in <trip>/photos/.

Usage:  python3 tools/make-gallery.py 2026-10-sengupta-family-singapore
Reads EXIF dates when Pillow is installed (pip install pillow); otherwise uses file dates.
Captions: add a "caption" to any entry in photos.json by hand — this script keeps them.
"""
import json, os, sys, datetime
trip = sys.argv[1].rstrip('/')
folder = os.path.join(trip, 'photos')
out = os.path.join(folder, 'photos.json')
keep = {}
if os.path.exists(out):
    try:
        for it in json.load(open(out)):
            keep[it['file']] = it.get('caption', '')
    except Exception:
        pass
def exif_date(path):
    try:
        from PIL import Image
        ex = Image.open(path).getexif()
        d = ex.get(36867) or ex.get(306)
        if d:
            return datetime.datetime.strptime(d, '%Y:%m:%d %H:%M:%S').isoformat()
    except Exception:
        pass
    return datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
items = []
for f in sorted(os.listdir(folder)):
    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
        items.append({'file': f, 'date': exif_date(os.path.join(folder, f)), 'caption': keep.get(f, '')})
json.dump(items, open(out, 'w'), indent=1, ensure_ascii=False)
print(f'{len(items)} photos → {out}')
