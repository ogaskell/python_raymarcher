import numpy as np
from tqdm import tqdm
import math

from .tools import Vector3


class Renderer:
    def __init__(self,
                 output_dimensions,
                 background,
                 shapes,
                 fov=120,
                 far_clipping_plane=11):

        self.dimensions = output_dimensions
        self.bg = background
        self.shapes = shapes
        self.camera = Camera(self.dimensions, fov)
        self.far_clipping_plane = far_clipping_plane

        self.clear()

    def clear(self):
        self.image = np.zeros(self.dimensions)

    def render(self):
        self.clear()

        for pixel_y in tqdm(range(self.dimensions[0]), desc="row"):  # Loop through rows

            for pixel_x in range(self.dimensions[1]):  # Loop through each pixel in row

                distance = 9999  # placeholder while distance isnt set
                P = Vector3()    # end of ray

                while distance > 0.02 and P.z < self.far_clipping_plane:  # hit something
                    distances = list(map(lambda x: x.dist(P), self.shapes))
                    distance = min(distances)

                    # print(distance)

                    P = self.camera.ray_pos([pixel_y, pixel_x], P.dist()+distance)

                if P.z < self.far_clipping_plane:
                    color = self.shapes[distances.index(sorted(distances)[0])].color
                    # print("Hit",self.shapes[distances.index(sorted(distances)[0])])
                else:
                    color = self.bg

                self.image[pixel_y, pixel_x] = color

        return self.image


class Camera:
    def __init__(self,
                 resolution,
                 fov):

        self.res = resolution
        self.aspect = resolution[1]/resolution[0]
        self.hfov = fov
        self.vfov = fov/self.aspect

        self.calculate_pixels()

    def pixel_pos(self,
                  screen_center: Vector3,
                  screen_tr: Vector3,
                  pix_ind):

        pix_width = (abs(screen_tr - screen_center)*2).x / self.res[1]
        # pix_height = (abs(screen_tr - screen_center)*2).y / self.res[0]
        pix_height = pix_width

        pix_x = (0.5 + pix_ind[1]) * pix_width
        pix_y = (0.5 + pix_ind[0]) * pix_height
        pix_z = screen_center.z

        return Vector3(pix_x,
                       pix_y,
                       pix_z)

    def calculate_pixels(self):
        pixel_positions = np.full(self.res, Vector3())

        for y in range(-self.res[0]//2, self.res[0]//2):
            for x in range(-self.res[1]//2, self.res[1]//2):
                pixel_positions[y, x] = self.pixel_pos(Vector3(0, 0, 1),
                                                       Vector3(math.tan(self.hfov/2),
                                                               math.tan(self.vfov/2),
                                                               1),
                                                       [y, x])

        self.pixels = pixel_positions

    def ray_pos(self,
                pix_ind,
                length):

        screen_pos = self.pixels[pix_ind[0], pix_ind[1]]

        normalised_pos = screen_pos/screen_pos.dist()

        return normalised_pos * length
