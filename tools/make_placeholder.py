"""Generates a placeholder 'micrograph' (grain structure) for the homepage.
Replace assets/img/hero.jpg with a real SEM/EBSD image when you have one."""
import numpy as np
from PIL import Image, ImageFilter
rng = np.random.default_rng(7)
W, H, N = 1600, 900, 140
pts = rng.random((N, 2)) * [W, H]
yy, xx = np.mgrid[0:H, 0:W]
best = np.full((H, W), np.inf); lab = np.zeros((H, W), int); second = np.full((H, W), np.inf)
for i, (px, py) in enumerate(pts):
    d = (xx - px) ** 2 + (yy - py) ** 2
    m = d < best
    second = np.where(m, best, np.minimum(second, d))
    lab = np.where(m, i, lab); best = np.where(m, d, best)
tone = rng.uniform(70, 200, N)[lab]
edge = (np.sqrt(second) - np.sqrt(best)) < 2.2
img = np.where(edge, 35, tone) + rng.normal(0, 9, (H, W))
# a few "precipitates"
for _ in range(220):
    cx, cy, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(1.5, 4)
    img[(xx - cx) ** 2 + (yy - cy) ** 2 < r * r] = 235
im = Image.fromarray(np.clip(img, 0, 255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.8))
im.save("assets/img/hero.jpg", quality=82)
print("saved")
