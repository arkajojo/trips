#!/usr/bin/env python3
"""Start a new visit folder and register it on the landing page.

Usage: python3 tools/new-trip.py <host: arka|nanki> <YYYY-MM-DD start> <YYYY-MM-DD end> "Title" ["subtitle"]
e.g.   python3 tools/new-trip.py nanki 2027-02-10 2027-02-24 "Mummy & Papa" "Nanki's parents · second visit"
Creates <host>/<YYYY-MM-slug>/ from _template and appends the trip to trips.json.
"""
import json, os, re, shutil, sys
host, start, end, title = sys.argv[1:5]; subtitle = sys.argv[5] if len(sys.argv) > 5 else ''
slug = start[:7] + '-' + re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
folder = os.path.join(host, slug)
shutil.copytree('_template', folder)
json.dump({'host': host, 'title': title, 'subtitle': subtitle, 'start': start, 'end': end, 'cover': '', 'albums': []}, open(os.path.join(folder, 'trip.json'), 'w'), indent=2)
m = json.load(open('trips.json'))
m['trips'].append({'host': host, 'folder': folder, 'title': title, 'subtitle': subtitle, 'start': start, 'end': end})
json.dump(m, open('trips.json', 'w'), indent=2, ensure_ascii=False)
print(f'created {folder}/ — now drop the itinerary in as index.html and the PDF as itinerary.pdf')
