# trips

Everyone who has come to stay with us in Singapore — the plan we made, and afterwards the photos.
Hosted on GitHub Pages: **https://arkajojo.github.io/trips/**

```
trips/
├── index.html           landing page — renders every visit from trips.json, grouped by host
├── trips.json           the list of visits (host, folder, title, dates)
├── arka/                Arka's side
│   └── 2026-10-treena-swapnadeep-ayanshi/
│       ├── index.html   itinerary + Memories (photos file themselves under the day they were taken)
│       ├── itinerary.pdf
│       ├── trip.json    dates, cover image, external album links
│       └── photos/      images + photos.json (+ thumbs/ generated)
├── nanki/               Nanki's side — same layout
├── _template/           what tools/new-trip.py copies
└── tools/               new-trip.py · make-gallery.py · resize.py
```

## New visit
```
python3 tools/new-trip.py nanki 2027-02-10 2027-02-24 "Mummy & Papa" "Nanki's parents"
```
Then put the itinerary in as `nanki/2027-02-mummy-papa/index.html`, the PDF as `itinerary.pdf`, push.

## After a visit
```
cp ~/Downloads/phone-export/*.jpg arka/2026-10-treena-swapnadeep-ayanshi/photos/
python3 tools/resize.py       arka/2026-10-treena-swapnadeep-ayanshi/photos     # shrink to web size, keeps EXIF dates
python3 tools/make-gallery.py arka/2026-10-treena-swapnadeep-ayanshi            # writes photos.json + thumbs/
git add -A && git commit -m "photos: Sengupta visit" && git push
```
Every photo lands under its day on the itinerary page (via EXIF date) and in the Memories gallery. Captions: edit `photos.json` by hand, the script keeps them. Google Photos / iCloud album links go in `trip.json` → `albums`; a cover image for the landing card goes in `trip.json` → `cover` (a file name inside `photos/`) and `trips.json` → `cover`.

## Publishing (one-time)
GitHub → this repo → **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save.**
Live a minute later at `https://arkajojo.github.io/trips/`; the Sengupta visit at `https://arkajojo.github.io/trips/arka/2026-10-treena-swapnadeep-ayanshi/`.

Public repo = public pages: no booking references, passport numbers or addresses in the pages, ever.
