import numpy as np
from PIL import Image

from shapes import *
from tools import *

#parameters
OUTPUT_WIDTH = 640
OUTPUT_HEIGHT = 360

BACKGROUND = [0,0,0]

#setup
imgdata = np.full([OUTPUT_HEIGHT,OUTPUT_WIDTH],
                  BACKGROUND)

#define shapes
shapes = [
          ]

#render


#create image
pil_img = Image.fromarray(imgdata,"RGB")
pil_img.show()
