from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Ensure it is a Path object
    filedir = filepath.parent  # Get directory from path

    # Create directory if it doesn't exist
    if filedir and not filedir.exists():
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    # Create file if it doesn't exist
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Creates an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
