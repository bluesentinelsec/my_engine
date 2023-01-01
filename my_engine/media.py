import io
import logging
import os
import sys
import zipfile


class MediaManager:
    def __init__(self, media_file: str = "data.dat"):
        self.media_file = media_file
        self.media_handle = ""
        self.fallback_to_real_file = False
        self.open_media_file()

    def open_media_file(self):
        try:
            self.media_handle = zipfile.ZipFile(self.media_file, "r", zipfile.ZIP_DEFLATED)
        except Exception as e:
            logging.debug(e)
            logging.debug("falling back to real file paths")
            self.fallback_to_real_file = True

    def get_file(self, file: str):
        if self.fallback_to_real_file:
            with open(file, "rb") as f:
                data = f.read()
                return io.BytesIO(data)
        else:
            data = self.media_handle.read(file)
            return io.BytesIO(data)

def create_media_file(out_file: str, media_directory: str):

    if not os.path.isdir(media_directory):
        logging.error(
            f"'{media_directory}' is not a directory")
        return

    dir_list = get_files_in_dir(media_directory)

    with zipfile.ZipFile(out_file, "w", zipfile.ZIP_DEFLATED) as zipper:
        for each_file in dir_list:
            zipper.write(each_file)


def get_files_in_dir(directory):
    files_in_dir = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            s = os.path.join(root, file)
            files_in_dir.append(s)
    return files_in_dir
