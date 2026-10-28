"""Copy root-level website files into the Sites publication directory."""
from pathlib import Path
from shutil import copy2, copytree

root = Path(__file__).resolve().parent
output = root / 'dist'
output.mkdir(exist_ok=True)
for name in ('index.html', 'style.css', 'app.js'):
    copy2(root / name, output / name)
copytree(root / 'assets', output / 'assets', dirs_exist_ok=True)
