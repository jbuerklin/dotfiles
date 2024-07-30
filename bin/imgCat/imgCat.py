#!/usr/bin/env python3
import os
import sys
from PIL import Image


class TerminalImageViewer():

    def __init__(self, path: str, sd: bool = None) -> None:
        self.image = Image.open(path)
        self.sd = sd
        self.initSize()
        self.initColors()

    def show(self) -> None:
        if self.sd:
            self.showImageSd()
        else:
            self.showImage()

    def initSize(self) -> None:
        size = list(self.image.size)
        max_y = os.get_terminal_size().lines - 1
        max_x = os.get_terminal_size().columns

        if not self.sd:
            max_y *= 2  # because every line is two pixels

        if size[1] > max_y:
            size[0] = size[0] / size[1] * max_y
            size[1] = max_y

        if size[0] > max_x:
            size[1] = size[1] / size[0] * max_x
            size[0] = max_x

        size[0] = int(size[0])
        size[1] = int(size[1])
        self.size = size
        self.image = self.image.resize(size)

    def initColors(self) -> None:
        self.image = self.image.quantize(colors=256, method=2)
        self.palette = {v: k for k, v in self.image.palette.colors.items()}

    def showImageSd(self) -> None:
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                color = self.getPixelColor(x, y)
                print(f'\u001b[48;5;{color}m  ', end='')
            print('\u001b[0m')


    def showImage(self) -> None:
        for y in range(0, self.size[1], 2):
            for x in range(self.size[0]):
                uppercolor = self.getPixelColor(x, y)
                try:
                    lowercolor = self.getPixelColor(x, y+1)
                except IndexError:
                    lowercolor = self.getPixelColor(x, y)
                print(f'\u001b[38;5;{lowercolor}m\u001b[48;5;{uppercolor}m\u2584', end='')
            print('\u001b[0m')


    def getPixelColor(self, x: int, y: int) -> int:
        pixel = self.image.getpixel((x, y))
        r, g, b, *a = self.palette.get(pixel, (0, 0, 0, 0))
        r = round(r / 255 * 5)
        g = round(g / 255 * 5)
        b = round(b / 255 * 5)
        return 16 + 36 * r + 6 * g + b

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()
    path = sys.argv[1]
    sd = '--sd' in sys.argv
    viewer = TerminalImageViewer(path, sd=sd)
    viewer.show()

