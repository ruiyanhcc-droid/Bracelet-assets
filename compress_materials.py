from pathlib import Path
from PIL import Image

RAW_DIR = Path("raw_materials")
OUT_DIR = Path("materials")

MAX_SIZE = 600  # 最长边 600px
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 支持的图片格式
EXTS = ["*.png", "*.jpg", "*.jpeg", "*.webp"]

files = []
for ext in EXTS:
    files.extend(list(RAW_DIR.glob(ext)))

print(f"Found {len(files)} images in {RAW_DIR}.")

for img_path in files:
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size

    scale = min(1.0, MAX_SIZE / max(w, h))
    new_size = (int(w * scale), int(h * scale))
    img = img.resize(new_size, Image.LANCZOS)

    out_path = OUT_DIR / img_path.name  # 保持同名
    out_path.parent.mkdir(parents=True, exist_ok=True)

    img.save(out_path, format="PNG", optimize=True)

    print(f"Compressed {img_path.name} -> {out_path} ({new_size[0]}x{new_size[1]})")

print("Done. Compressed images are in 'materials/'.")

