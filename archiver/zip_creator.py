import zipfile
import pathlib

def create_archive(filepaths, dest_dir):
    with zipfile.ZipFile(pathlib.Path(dest_dir, "compressed.zip"), "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath)
