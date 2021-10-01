import tempfile
import zipfile
from pathlib import Path

import wget


def download_from_url(url: str, dest_path: Path, verbose: bool = False) -> None:
    """Download item from url to dest_path."""

    assert (
        dest_path.parent.exists()
    ), 'Parent folder of destination path does not exist.'

    if verbose:
        print(f'Downloading from {url} to {dest_path}.')

    wget.download(out=str(dest_path), url=url)


def download_zip_from_url(url: str, dest_folder: Path, verbose: bool = False) -> None:
    """Download from url to tempfolder and then unzip to dest_folder."""
    if verbose:
        print(f'Downloading from {url} to {dest_folder}.')

    with tempfile.TemporaryDirectory() as tmpdirname:
        zip_file = f'{tmpdirname}/{dest_folder.stem}.zip'

        wget.download(out=zip_file, url=url)
        with zipfile.ZipFile(zip_file) as z:
            z.extractall(dest_folder)

    assert dest_folder.exists()
