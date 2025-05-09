import logging
from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path
from typing import Literal

from PIL import Image

from util.timer import timer
from helper import bright

logger = logging.getLogger(__name__)


class Picture:
    def __init__(self, path: Path):
        try:
            self.image_file = Image.open(path)
            self.image = self.image_file.load()
            self.width = self.image_file.width
            self.height = self.image_file.height
            self.img_array=[[0] * self.height for _ in range(self.width)]
        except Exception as e:
            logger.error(
                f"There was an error while loading the image {path}. Reason {e}"
            )

    @timer
    def brighten(self, intensity: float):
        for i in range(self.width):
            for j in range(self.height):
                self.img_array[i][j] = self.img_array[i][j] + 1
                self.image[i, j] = bright(self.image[i, j], intensity)


    def _submit(self, func, i, j, **kwargs):
        # print(i,j)
        self.img_array[i][j] += 1
        pixel = self.image[i,j]
        return func(pixel, **kwargs), i, j

    def _apply(self, future):
        rgb, i, j = future.result()
        self.image[i,j] = rgb

    @timer
    def brighten_concurrent(self, intensity: float):
        with ThreadPoolExecutor(max_workers=1) as worker:
            for i in range(self.width):
                for j in range(self.height):
                    future = worker.submit(self._submit,bright, i, j, intensity=intensity)
                    future.add_done_callback(self._apply)

    # def blur(self, intensity: float):
    #     original_image = self.image
    #     lookup_radius_width = int(self.width * 0.3 * intensity)
    #     lookup_radius_height = int(self.height * 0.3 * intensity)
    #     for i in range(self.width - lookup_radius_width):
    #         for j in range(self.height - lookup_radius_height):
    #             neighbouring_pixel_rgb = (0,0,0)
    #             for w in range(i, i + lookup_radius_width):
    #                 for h in range(j, j+lookup_radius_height):

    @timer
    def export(self, path: Path, export_format: Literal["PNG", "JPEG"] = "PNG"):
        try:
            self.image_file.save(fp=path, format=export_format)
        except Exception as e:
            logger.error(f"Unable to export image to file {path}. Reason {e}")


if __name__ == "__main__":
    pic = Picture(Path("../resources/images/saad-chaudhry-cYpqYxGeqts-unsplash.jpg"))
    # pic.brighten(0.8)
    pic.brighten_concurrent(0.8)
    pic.export(Path("../resources/output/export-bright.jpg"))
    print(pic.img_array)
