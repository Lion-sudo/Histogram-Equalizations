import abc
import numpy as np


# Constants
NUMBER_OF_GRAY_VALUES = 256
MAX_GRAY_VALUE = 255
EMPTY_HISTOGRAM_CODE = -1
EMPTY_HISTOGRAM_EXCEPTION = "Image is empty."
ONE_SHADE_OF_GRAY_EXCEPTION = "Image only has one shade of gray, can't apply histogram equalization."


class AbstractHistogramEqualizer(metaclass=abc.ABCMeta):
    def extract_minimal_shade(self, hist):
        for i in range(NUMBER_OF_GRAY_VALUES):
            if hist[i] > 0:
                return i
        return EMPTY_HISTOGRAM_CODE

    def histogram_equalization(self, image):
        # 1) compute the cumulative image histogram
        hist, _ = np.histogram(image.flatten(), bins=NUMBER_OF_GRAY_VALUES, range=[0, NUMBER_OF_GRAY_VALUES])
        hist = np.cumsum(hist)

        # 2) normalize the cumulative histogram
        total_pixels = image.size
        hist = hist / total_pixels  # divide by total number of pixels

        min_gray = self.extract_minimal_shade(hist)  # first gray shade with >= 1 pixels
        if min_gray == EMPTY_HISTOGRAM_CODE:
            raise Exception(EMPTY_HISTOGRAM_EXCEPTION)
        min_value = hist[min_gray]
        max_value = hist[-1]

        if min_value == max_value:
            raise Exception(ONE_SHADE_OF_GRAY_EXCEPTION)

        hist = MAX_GRAY_VALUE * ((hist - min_value) / (max_value - min_value))
        hist = np.round(hist).astype(np.uint8)

        # 3) map the intensity values of the image
        equalized_image = hist[image]
        return equalized_image

    @abc.abstractmethod
    def equalize(self, image, input_id):
        pass

