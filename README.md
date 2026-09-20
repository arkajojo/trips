# trips

Every visit we host in Singapore gets its own folder here: the itinerary as a web page, the PDF, and later the photos.
Hosted with GitHub Pages, so each folder is a shareable link.

```
trips/
├── index.html                              ← landing page listing every trip
├── 2026-10-sengupta-family-singapore/      ← one folder per visit: YYYY-MM-who-where
│   ├── index.html                          ← the itinerary (self-contained page)
│   ├── itinerary.pdf
│   ├── photos.html                         ← gallery, renders whatever is in photos/photos.json
│   └── photos/                             ← drop images here, then run the tool below
├── _template/                              ← copy this to start the next visit
└── tools/make-gallery.py                   ← rebuilds photos/photos.json from the folder
```

## Adding a new trip
1. Copy `_template/` to a new folder named `YYYY-MM-who-where`.
2. Replace `index.html` with the itinerary page; drop the PDF in as `itinerary.pdf`.
3. Add a card for it in the root `index.html`.
4. Commit and push — Pages redeploys in about a minute.

## Adding photos after a trip
1. Copy images (jpg / png / webp / heic-converted-to-jpg) into `<trip>/photos/`. Keep them under ~2 MB each; `tools/resize.py` shrinks a folder in place.
2. Run `python3 tools/make-gallery.py <trip-folder>` — it writes `photos/photos.json` with every image and its date.
3. Commit and push. `<trip>/photos.html` shows them newest-first with lightbox.

## Publishing (one-time)
```
git init && git add . && git commit -m "trips: Sengupta family, Oct 2026"
gh repo create trips --public --source=. --push     # or create the repo on github.com and `git remote add origin ...`
```
Then on GitHub: **Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save.**
The site is live at `https://<username>.github.io/trips/` and this trip at `https://<username>.github.io/trips/2026-10-sengupta-family-singapore/`.

Note: a public repo is public. Booking references and passport details are deliberately not in the pages; keep it that way.
