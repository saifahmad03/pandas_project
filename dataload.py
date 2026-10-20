import kagglehub
import shutil
from pathlib import Path

# Download to kagglehub's cache
path = kagglehub.dataset_download("heesoo37/120-years-of-olympic-history-athletes-and-results")
print("Downloaded to:", path)

# Copy the CSVs into the project
dest = Path("data/raw")
dest.mkdir(parents=True, exist_ok=True)
for f in Path(path).glob("*.csv"):
    shutil.copy(f, dest / f.name)
    print("Copied", f.name)