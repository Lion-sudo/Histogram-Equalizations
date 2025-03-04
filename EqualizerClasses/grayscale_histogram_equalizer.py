import cv2
from EqualizerClasses.abstract_histogram_equalizer import AbstractHistogramEqualizer


# Constants
GRAYSCALE_RESULT_PATH = "grayscale_output.jpg"
SUCCESS_MSG = "Finished grayscale histogram equalization successfully."


class GrayscaleHistogramEqualizer(AbstractHistogramEqualizer):
    def equalize(self, image, input_id):
        # 1) convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 2) equalize the gray channel and save the image
        cv2.imwrite(f"image_{input_id}_{GRAYSCALE_RESULT_PATH}", self.histogram_equalization(image))
        print(SUCCESS_MSG)
