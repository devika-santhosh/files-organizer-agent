import os
import shutil
from pathlib import Path

# Define your Downloads path
DOWNLOADS_DIR = os.getcwd()

# Define categories and their extensions
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Code": [".py", ".js", ".html", ".css", ".ipynb"],
    "Others": []
}

def categorize_file(file):
    ext = file.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_downloads():
    for file in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file)
        if os.path.isfile(file_path):
            category = categorize_file(Path(file_path))
            target_dir = os.path.join(DOWNLOADS_DIR, category)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(target_dir, file))

if __name__ == "__main__":
    organize_downloads()

