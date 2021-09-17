import cv2
import numpy as np


class Image:
    def __init__(self):
        pass

    def read(self, path: str) -> np.array:
        img = cv2.imread(path)
        return img
        # Todo: загрузка изображения

    def show(self, color: str) -> None:
        color_img = cv2.cvtColor(self, getattr(cv2, 'COLOR_BGR2' + color))
        cv2.imshow('Color' + color, color_img)
        cv2.waitKey(0)
        # Todo: отрисовка издбражения

    def save(self, path: str) -> None:
        cv2.imwrite(path, self)

        # Todo: сохранение издбражения

    def calc_hist(self, color: str, channels: list, bins_per_channel: list,
                  range_hist: list) -> np.array:
        if color == 'rgb':
            rgb = cv2.cvtColor(self, cv2.COLOR_BGR2RGB)
            hist = cv2.calcHist([rgb], channels, None, bins_per_channel, range_hist)
        elif color == 'hsv':
            hsv = cv2.cvtColor(self, cv2.COLOR_BGR2HSV)
            hist = cv2.calcHist([hsv], channels, None, bins_per_channel, range_hist)
        elif color == 'lab':
            lab = cv2.cvtColor(self, cv2.COLOR_BGR2LAB)
            hist = cv2.calcHist([lab], channels, None, bins_per_channel, range_hist)
        else:
            print('Input normal color')
        return hist
        # Todo: вычисление гистограммы, для color - 'rgb', 'lab', 'hsv'


def hist_compare(a: Image, b: Image, color: str, channels: list, bins_per_channel: list,
                 method: str, range_hist: list) -> float:
    hist_1 = a.calc_hist(color, channels, bins_per_channel, range_hist)
    hist_2 = b.calc_hist(color, channels, bins_per_channel, range_hist)
    compare_result = cv2.compareHist(hist_1, hist_2, method)
    return compare_result
    # Todo: реализовать сравнение двух гистограм, method соответствует method в cv2.compareHist















