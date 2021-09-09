from pathlib import Path
import tempfile
import zipfile
from pathlib import Path

import wget


def download_zip_from_url(url: str, dest_folder: Path) -> None:
    with tempfile.TemporaryDirectory() as tmpdirname:
        zip_file = f'{tmpdirname}/{dest_folder.stem}.zip'

        wget.download(out=zip_file, url=url)
        with zipfile.ZipFile(zip_file) as z:
            z.extractall(dest_folder)

    assert dest_folder.exists()
