"""Copy root-level website files into the Sites publication directory."""
from pathlib import Path
from shutil import copy2, copytree, rmtree

root = Path(__file__).resolve().parent
output = root / 'dist'
output.mkdir(exist_ok=True)
for name in ('index.html', 'style.css', 'app.js', 'site.webmanifest'):
    copy2(root / name, output / name)
if (output / 'assets').exists():
    rmtree(output / 'assets')
copytree(root / 'assets', output / 'assets')
