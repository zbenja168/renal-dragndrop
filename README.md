# RenalStudy — Drag & Drop Games

67 self-contained drag-and-drop matching games covering renal & urinary medicine, generated from 21 source bricks (week 1).

## Use

Open `renal_index.html` in a browser. No build step, no server needed — every file is plain HTML/CSS/JS.

## Layout

- `renal_index.html` — landing page with search and brick-grouped sections
- `renal_NN_<slug>.html` — individual game files (67 total), each with a different accent from an 8-color rotating palette
- `_gen_renal.py` — generator script
- `renal_data/brick_NN.py` — extracted facts per brick that drive each game

## Topics covered (21 bricks)

Anatomy of the urinary system · Embryology · Congenital kidney disorders · Histology · Glomerular function · GFR · Renal clearance · RBF regulation · Nephron physiology · Sodium homeostasis · Potassium homeostasis · Loop diuretics · Thiazides · Osmotic diuretics · K+-sparing diuretics · Body fluids & compartments · Water regulation · Hyponatremia · Hypernatremia · ADH agonists · ADH antagonists

## Regenerating

```
python _gen_renal.py
```

This rewrites all `renal_*.html` files from `renal_data/`.
