import os
from pathlib import Path

# Name of the package to be used in file paths
package_name = "database_connector"

# List of files and directories to create for the project structure
list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiment.ipynb"
]

# Iterate through each file path in the list
for file_path in list_of_files:
    file_path = Path(file_path)  # Convert to Path object for consistency

    # Split the file path into directory and file name
    file_dir, file_name = os.path.split(file_path)

    # Create the directory if it doesn't exist
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass  # Create an empty file
