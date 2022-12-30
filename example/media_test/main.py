# gross hack to import from parent directories
import sys
import os

sys.path.insert(1, os.path.join(sys.path[0], '../../'))
import my_engine.media as m

media = m.MediaManager()
data = media.get_file("image.png")
print(f"read media with length: {len(data)}")

