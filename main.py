import my_engine.tiled_loader as ll
import logging
import sys

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s (%(filename)s:%(lineno)s) %(message)s')

    level_file = sys.argv[1]
    level_loader = ll.LevelLoader()
    level_loader.load_level(level_file)
    #level_loader.print_level_data()
    level_loader.parse_level_data()

if __name__ == "__main__":
    main()