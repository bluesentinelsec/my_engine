import io
import logging
import sys
import zipfile


class MediaManager:
    def __init__(self, media_file: str):
        self.media_file = media_file
        self.media_handle = ""
        self.open_media_file()

    def open_media_file(self):
        try:
            self.media_handle = zipfile.ZipFile(self.media_file, "r", zipfile.ZIP_DEFLATED)
        except Exception as e:
            logging.fatal(e)
            sys.exit(-1)

    def get_file(self, file: str):
        data = self.media_handle.read(file)
        return io.BytesIO(data)
