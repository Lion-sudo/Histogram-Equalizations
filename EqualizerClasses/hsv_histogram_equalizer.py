import cv2
from EqualizerClasses.abstract_histogram_equalizer import AbstractHistogramEqualizer


# Constants
HSV_RESULT_PATH = "hsv_output.jpg"
SUCCESS_MSG = "Finished HSV histogram equalization successfully."


class HsvHistogramEqualizer(AbstractHistogramEqualizer):
    def equalize(self, image):
        # 1) convert to HSV color and split the channels
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv_image)

        # 2) equalize the V channel and merge the channels
        equalized_v = self.histogram_equalization(v)
        equalized_hsv_image = cv2.merge([h, s, equalized_v])

        # 3) convert back to BGR color and return
        cv2.imwrite(HSV_RESULT_PATH, cv2.cvtColor(equalized_hsv_image, cv2.COLOR_HSV2BGR))
        print(SUCCESS_MSG)