import zipfile

def extract_archive(archivepath, dest_Dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_Dir)

# if __name__ == "__main__":
    # extract_archive("C:\Users\piotr\Github\Python\Python\Ardit\FileCompress\Compressed.zip", "C:\Users\piotr\Github\Python\Python\Ardit\FileCompress")