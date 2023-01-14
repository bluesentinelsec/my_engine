import logging
import xml.etree.ElementTree as ET


class SceneLoader:
    def __init__(self) -> None:
        logging.debug("creating SceneLoader instance")

    def read_scene_file(self, file):
        logging.debug(f"reading scene file: {file}")

        tree = ET.parse(file)
        entities_root = tree.getroot()

        print()

        # get each entity
        for each_entity in entities_root:
            s = each_entity.attrib
            logging.debug(f"creating entity of type: {s['type']}")
            # ToDo - create entity object

            # from the root component element
            for components in each_entity:

                # get each component
                for component in components:
                    s = component.attrib

                    # process each component based on its type
                    print(f"found component of type: {s['type']}")
                    if s["type"] == "transform":
                        print(
                            f"x_position: {s['x_position']} - y_position: {s['y_position']}")
                        # create transform component
                        # append component to entity

                    elif s["type"] == "sprite":
                        print(f"image_file: {s['image_file']}")
                        # create sprite component
                        # append component to entity

                    else:
                        logging.debug(
                            f"found unknown component of type: {s['type']}")

            print()
