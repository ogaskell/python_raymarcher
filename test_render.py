from PIL import Image
import sys

from raymarcher.primitives import Sphere
from raymarcher.tools import Vector3

from raymarcher.march import Renderer

params = sys.argv
if len(sys.argv) == 1:
    OUTPUT_WIDTH, OUTPUT_HEIGHT = 320, 240
    BACKGROUND = 0

if len(sys.argv) == 3:
    OUTPUT_WIDTH, OUTPUT_HEIGHT = map(int, sys.argv[1].split(","))
    BACKGROUND = map(int, sys.argv[2].split(","))

elif len(sys.argv) == 4:
    OUTPUT_WIDTH, OUTPUT_HEIGHT = map(int, sys.argv[1].split(","))
    BACKGROUND = map(int, sys.argv[2].split(","))
    FILENAME = sys.argv[3]

# define shapes
shapes = [Sphere(center=Vector3(0, 0, 5),
                 radius=1),
          # Sphere(center = Vector3(3,-1,8),
          #        radius = 0.6,
          #        color=255),
          # Sphere(center = Vector3(2,2,10),
          #        radius = 1.2,
          #        color=60),
          ]

# render
engine = Renderer((OUTPUT_HEIGHT, OUTPUT_WIDTH),
                  BACKGROUND,
                  shapes)

print("Beginning render")
image = engine.render()

# create image
pil_img = Image.fromarray(image)
pil_img.show()
