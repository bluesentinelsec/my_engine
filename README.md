# My_Engine

My_Engine is a simple game engine built on top of the PyGame framework.

My_Engine was created to learn about creating game engines, with a deisgn goal of making it easy to create entities and levels using only code.

## Installation

```
pip install my_engine
```

## Quick Start

0. **Package your media**

My_Engine reads media files from a single zip archive named `data.dat` by default.

To create a packed media archive, run the following:

```bash
# recursively zip the folder 'media'
# and produce an output file of 'data.dat'
zip -r data.dat media/

# note 1: assume media contains all of your images, sound files, etc.
# note 2: place your data.dat file in the same folder as your program
```

You will use the built in [media manager](my_engine/media.py) to load media into your game.

1. **Create a game entity** 

Entities are the lowest level element in My_Engine.

Entities can be dynamic characters like sprites, or static resources such as backgrounds.

See example [here](example/OpenPyPong/player.py)

2. **Create a scene**

Scenes are essentially game screens or levels.

Scenes are made up of entities.

See example [here](example/OpenPyPong/scene_gameplay.py)

3. **Initialize the game**

Create your game's `main.py` file.

See example [here](example/OpenPyPong/main.py)

4. **Package your game**

We reccomend using PyInstaller to package your game:

```bash
# pack your game into a single exe
pyinstaller --onefile main.py

# view your exe
ls -lsah dist/

# place your packed media file with the game exe
cp data.dat dist/

# zip your dist folder
zip -r my_game.zip dist/
```

At this point, you can upload `my_game.zip` to wherever you're hosting your game.

End users need only download and unzip your file and run your game exe.