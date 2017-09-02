#!/usr/bin/env python
import imghdr
from PIL import Image
import os
import logging
import sys

directory = os.fsencode("./images")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    try:
        im = Image.open(sys.argv[1] + filename)
        base=os.path.basename(sys.argv[1] + filename)
        im.verify()
        im = Image.open(sys.argv[1] + filename)
        im.load()
        try:
            if (imghdr.what(sys.argv[1] + filename) != "jpeg" or imghdr.what(sys.argv[1] + filename) != "jpg"):
                rgb_im = im.convert('RGB')
                rgb_im.save(sys.argv[1] + os.path.splitext(base)[0] + ".jpg")
                os.remove(sys.argv[1] + filename)
        except Exception as e:
            os.remove(sys.argv[1] + filename)
    except Exception as e:
        os.remove(sys.argv[1] + filename)
    
