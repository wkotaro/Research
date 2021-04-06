#!/usr/bin/env python

import glob

from PIL import Image

frames = []
images = glob.glob("../original/cylinder_46/*.jpg")

for image in images:
    new_frame = Image.open(image)
    frames.append(new_frame)
    new_frame.load()

print(frames)
frames[0].save('../movie/cylinder46.gif',
                format='GIF',
                append_images=frames[1:200],
                save_all=True,
                duration=600,
                loop=0)
