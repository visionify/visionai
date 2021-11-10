import cv2
import numpy as np
from matplotlib import pyplot as plt
from colorthief import ColorThief

def convert_to_256(img_name):
    frame = cv2.imread(img_name)

    div = 32
    quantized = frame // div * div + div // 2
    cv2.imwrite('quantized-' + img_name, quantized)

def histogram(img_name):
    img = cv2.imread(img_name)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

def get_dominant_color(img_name):
    color_theif = ColorThief(img_name)
    palette = color_theif.get_palette(color_count=100)
    return palette

def remove_palette(img_name, quantized_img_name, palette):
    # frame = cv2.imread(img_name)
    quantized = cv2.imread(quantized_img_name)
    w, h, _ = quantized.shape
    for x in range(w):
        for y in range(h):
            val = tuple(quantized[x][y])
            if val in palette:
                quantized[x][y] = (0, 0, 255)

    cv2.imwrite('output-' + img_name, quantized)

if __name__ == '__main__':
    palette = get_dominant_color('quantized-choco-chip.jpg')
    # convert_to_256('choco-chip.jpg')
    # histogram('quantized-choco-chip.jpg')
    remove_palette('choco-chip.jpg', 'quantized-choco-chip.jpg', palette)




