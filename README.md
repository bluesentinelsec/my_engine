# My_Engine

My_Engine is a simple game engine built on top of the PyGame framework.

My_Engine was created to learn about creating game engines, with a deisgn goal of making it easy to create entities and levels using only code.

## Pardon our dust

This repository is under active development.

This project should be considered unstable and unusable until this message is removed.

## Prerequisites

Install Python 3 and Pip for your platform.


## Quick Start

Install my_engine:

```bash
pip install my_engine
```

Clone the repo:

```bash
git clone https://github.com/bluesentinelsec/my_engine.git
```

Test installation:

```bash
cd my_engine/example/OpenPyPong

python main.py
```

Take a look at the OpenPyPong source to see how to build a simple game.

## Workflow

### 1. Package your media

My_Engine reads media files from a single zip archive named `data.dat` by default.

This is so that we do not need to ship a ton of media files at deploy time.

To create a packed media archive, run the following:

```bash
# recursively zip the folder 'media'
# and produce an output file of 'data.dat'
zip -r data.dat media/

# note 1: assume media contains all of your images, sound files, etc.

# note 2: place your data.dat file in the same folder as your program
```

You will use the built in [media manager](my_engine/media.py) to load media into your game.

### 2. Create a game entity

Entities are the lowest level element in My_Engine.

Entities can be dynamic characters like sprites, or static resources such as backgrounds.

See: [example/OpenPyPong/player.py](example/OpenPyPong/player.py).

### 3. Create a scene

Scenes are essentially game screens or levels.

Scenes are made up of entities.

See: [example/OpenPyPong/scene_gameplay.py](example/OpenPyPong/scene_gameplay.py).

### 4. Create entry point

Create your game's `main.py` file.

See: [example/OpenPyPong/main.py](example/OpenPyPong/main.py).

### 5. Package your game

We reccomend using PyInstaller to package your game:

```bash
# pack your game into a single exe
# if targetting Windows, pass a '--noconsole' argument
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

Be sure to test your deploy package on target systems, as there are quite a few gotchas with PyInstaller.
