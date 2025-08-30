import random, shutil
from pathlib import Path

random.seed(42)
SRC_IMAGES = Path("dataset/images")
SRC_LABELS = Path("dataset/labels")
DEST = Path("data")

DEST.mkdir(exist_ok=True)

imgs = sorted([p for p in SRC_IMAGES.iterdir() if p.suffix.lower() in [".jpg", ".jpeg", ".png"]])
n = len(imgs)
n_train = int(0.8 * n)
n_val = int(0.1 * n)

splits = {
    "train": imgs[:n_train],
    "val": imgs[n_train:n_train+n_val],
    "test": imgs[n_train+n_val:]
}

for split, files in splits.items():
    img_out = DEST / split / "images"
    lbl_out = DEST / split / "labels"
    img_out.mkdir(parents=True, exist_ok=True)
    lbl_out.mkdir(parents=True, exist_ok=True)
    for imgp in files:
        shutil.copy(imgp, img_out / imgp.name)
        lbl = SRC_LABELS / (imgp.stem + ".txt")
        if lbl.exists():
            shutil.copy(lbl, lbl_out / lbl.name)
        else:
            open(lbl_out / (imgp.stem + ".txt"), "w").close()

print("Split sizes:", {k: len(v) for k,v in splits.items()})
