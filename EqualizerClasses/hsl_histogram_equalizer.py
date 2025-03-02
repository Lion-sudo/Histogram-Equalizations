import cv2
from EqualizerClasses.abstract_histogram_equalizer import AbstractHistogramEqualizer

# Constants
HSL_OUTPUT_PATH = "hsl_output.jpg"
SUCCESS_MSG = "Finished HSL histogram equalization successfully."

class HSLHistogramEqualizer(AbstractHistogramEqualizer):
    def equalize(self, image, input_id):
        # 1) convert the image to HSL and split the channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
        H, L, S = cv2.split(image)

        # 2) equalize the Lightness channel and merge the channels
        equalized_L = self.histogram_equalization(L)
        equalized_hsl = cv2.merge([H, equalized_L, S])

        # 3) convert to BGR and save the image
        cv2.imwrite(f"image_{input_id}_{HSL_OUTPUT_PATH}", cv2.cvtColor(equalized_hsl, cv2.COLOR_HLS2BGR))
        print(SUCCESS_MSG)
