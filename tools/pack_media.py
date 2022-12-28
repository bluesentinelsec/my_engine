#!/usr/bin/env python3

import argparse
import logging
import os
import zipfile


def create_media_file(out_file: str, media_directory: str):

    if not os.path.isdir(media_directory):
        logging.error(
            f"'{media_directory}' is not a directory")
        return

    # save current working directory for later
    current_dir = os.getcwd()

    # enter media folder's parent directory
    # so our packed media file has correct file paths
    os.chdir(f"{media_directory}/../")
    
    # list all files in media directory
    dir_list = get_files_in_dir(media_directory)
    
    # return to original working directory
    os.chdir(current_dir)

    # write media files to a zip archive
    with zipfile.ZipFile(out_file, "w", zipfile.ZIP_DEFLATED) as zipper:
        for each_file in dir_list:
            zipper.write(each_file)

    # ToDo: password encrypt media file

def get_files_in_dir(directory):
    files_in_dir = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            s = os.path.join(root, file)
            files_in_dir.append(s)
    return files_in_dir


def main(args):
    # setup console logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')
        logging.debug("enabled verbose console logging")

    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    create_media_file(args.out, args.media_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("media_folder", type=str)
    parser.add_argument("-o", "--out", type=str,
                        required=False, default="data.dat")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    main(args)
