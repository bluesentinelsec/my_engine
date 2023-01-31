"""
tiled_parser reads Tiled TMX
files and instantiates the
map's tiles, images, and objects.

See tiled_parser_test.py for example
usage.

"""
from pytmx.util_pygame import load_pygame
import pytmx
import pygame


class TiledSprite:
    """
    TiledSprite is used to store data
    for each tile in a Tiled map file.
    """

    def __init__(self, x, y, w, h, img, gid):
        # x position
        self.x = x

        # y position
        self.y = y

        # sprite width
        self.w = w

        # sprite height
        self.h = h

        # sprite image - is a Surface when used with PyGame
        self.img = img

        # unique ID
        self.gid = gid


class TiledParser:
    """
    TiledParser is used to parse
    Tiled maps in XML format (.tmx).
    To access the parsed tiles, iterate
    over the following lists:
    - self.tile_layer_objects
    - self.background_layer_objects
    - self.object_layer_objects
    """

    def __init__(self):
        # stores instances of tile layer entities (tiles)
        # the calling function should iterate over this list
        # to create/update/draw this object in game
        self.tile_layer_objects = []

        # stores instances of static image entities (images)
        # the calling function should iterate over this list
        # to create/update/draw this object in game
        self.background_layer_objects = []

        # stores instances of object layer entities (actors)
        # the calling function should iterate over this list
        # to create/update/draw this object in game
        self.object_layer_objects = []

        # stores XML after reading source tiled map file
        self.map_data = ""

    def parse_map(self, map_file):
        """
        reads the provided tiled map file
        and instantiates each tile/image/object
        """

        try:
            # read the source tiled file (.tmx)
            self.map_data = load_pygame(map_file)
        except Exception as e:
            raise e

        # get all layers from map file
        layers = self.map_data.layers

        # iterate over each layer
        for each_layer in layers:

            # parse image layer (i.e. layers containing only static images)
            if isinstance(each_layer, pytmx.TiledImageLayer):
                self.parse_image_layer(each_layer)

            # parse tile layer (i.e. layers containing floor/wall tiles)
            elif isinstance(each_layer, pytmx.TiledTileLayer):
                self.parse_tile_layer(each_layer)

            # parse object layer (i.e. layers containing dynamic objects)
            # like the player character or enemies
            elif isinstance(each_layer, pytmx.TiledObjectGroup):
                self.parse_object_layer(each_layer)

            else:
                raise f"unknown layer: {each_layer} - {type(each_layer)}"

    def parse_image_layer(self, each_layer):
        """
        parses a tiled map image layer
        and store image objects in
        the 'background_layer_objects' list
        """

        # get the image surface
        img_surface = each_layer.image

        # create a background sprite
        background_sprite = TiledSprite(x=0,
                                        y=0,
                                        w=img_surface.get_width(),
                                        h=img_surface.get_height(),
                                        img=img_surface,
                                        gid=6)

        # add background sprite to list
        self.background_layer_objects.append(background_sprite)

    def parse_tile_layer(self, each_layer):
        """
        parses a tiled map image layer
        and store image objects in
        the 'tile_layer_objects' list
        """

        # get each cell's x,y, and gid from layer
        for cellx, celly, gid in each_layer:

            # skip empty cells
            if gid == 0:
                continue

            # get image / PyGame surface from each cell GID
            img = self.map_data.get_tile_image_by_gid(gid)
            if not img:
                print(f"did not get image from element with GID: {gid}")
                continue

            # create new tile sprite
            tile_sprite = TiledSprite(x=cellx * self.map_data.tilewidth,
                                      y=celly * self.map_data.tileheight,
                                      w=img.get_width(),
                                      h=img.get_height(),
                                      img=img,
                                      gid=gid)

            # add tile sprite to list
            self.tile_layer_objects.append(tile_sprite)

    def parse_object_layer(self, each_layer):
        """
        parses a tiled map object layer
        and store image objects in
        the 'object_layer_objects' list
        """

        for obj in each_layer:

            # skip empty objects
            if obj.gid == 0:
                continue

            # scale the sprite's image/surface to match
            # the scale specified in the Tiled map
            scaled_image = pygame.transform.scale(obj.image, (obj.width, obj.height))

            # create the new actor object
            o = TiledSprite(x=obj.x,
                            y=obj.y,
                            w=obj.width,
                            h=obj.height,
                            img=scaled_image,
                            gid=obj.gid)

            # append object to list
            self.object_layer_objects.append(o)

"""
map_parser = tiled_parser.TiledParser()
map_parser.parse_map("map.tmx")

...

   # draw background
    for background in map_parser.background_layer_objects:
        screen.blit(background.img, (background.x, background.y))

    # draw tiles
    for each_spr in map_parser.tile_layer_objects:
        print(f"blitting sprite: {each_spr.gid}")
        screen.blit(each_spr.img, (each_spr.x, each_spr.y))

    # draw dynamic objects
    for each_obj in map_parser.object_layer_objects:
        screen.blit(each_obj.img, (each_obj.x, each_obj.y, each_obj.w, each_obj.h))

"""