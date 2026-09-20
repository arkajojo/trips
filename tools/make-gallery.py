#!/usr/bin/env python3
"""Rebuild photos/photos.json for one trip, filing each photo under the day it was taken.

Usage:  python3 tools/make-gallery.py arka/2026-10-treena-swapnadeep-ayanshi
Reads the trip's start date from trip.json, EXIF dates from the images (pip install pillow),
keeps any captions you've typed into photos.json by hand, and makes a small thumb for each image.
"""
import json, os, sys, datetime
trip = sys.argv[1].rstrip('/')
folder = os.path.join(trip, 'photos'); out = os.path.join(folder, 'photos.json')
meta = json.load(open(os.path.join(trip, 'trip.json')))
start = datetime.date.fromisoformat(meta['start'])
keep = {}
if os.path.exists(out):
    try:
        for it in json.load(open(out)): keep[it['file']] = it
    except Exception: pass
try:
    from PIL import Image, ImageOps
except ImportError:
    Image = None
def exif_date(path):
    if Image:
        try:
            ex = Image.open(path).getexif(); d = ex.get(36867) or ex.get(306)
            if d: return datetime.datetime.strptime(d, '%Y:%m:%d %H:%M:%S').isoformat()
        except Exception: pass
    return datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
os.makedirs(os.path.join(folder, 'thumbs'), exist_ok=True)
items = []
for f in sorted(os.listdir(folder)):
    if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')): continue
    path = os.path.join(folder, f)
    date = keep.get(f, {}).get('date') or exif_date(path)
    day = (datetime.date.fromisoformat(date[:10]) - start).days + 1
    it = {'file': f, 'date': date, 'day': keep.get(f, {}).get('day') or (day if day >= 1 else 0), 'caption': keep.get(f, {}).get('caption', '')}
    if Image:
        tp = os.path.join(folder, 'thumbs', os.path.splitext(f)[0] + '.jpg')
        if not os.path.exists(tp):
            im = ImageOps.exif_transpose(Image.open(path)); im.thumbnail((480, 480)); im.convert('RGB').save(tp, quality=80)
        it['thumb'] = 'thumbs/' + os.path.basename(tp)
    items.append(it)
json.dump(items, open(out, 'w'), indent=1, ensure_ascii=False)
print(f'{len(items)} photos → {out}')
