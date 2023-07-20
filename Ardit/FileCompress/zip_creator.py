import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    # with zipfile.ZipFile(dest_dir + "/" + "compressed.zip", 'w') as archive:
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths=["1.txt", "2.txt"], dest_dir="dest")