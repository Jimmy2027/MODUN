import zipfile
from pathlib import Path


def unzip_to(path_to_zip_file: Path, dest_path: Path, verbose: bool = False) -> None:
    """Unzip file to destination folder."""
    if verbose:
        print(f'unzipping {path_to_zip_file} to {dest_path}.')
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_path)
