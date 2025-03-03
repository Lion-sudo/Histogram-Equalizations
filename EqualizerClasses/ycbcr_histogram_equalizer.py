import cv2
from EqualizerClasses.abstract_histogram_equalizer import AbstractHistogramEqualizer


# Constants
YCBCR_OUTPUT_PATH = "ycbcr_output.jpg"
SUCCESS_MSG = "Finished YCbCr histogram equalization successfully."

class YCBCRHistogramEqualizer(AbstractHistogramEqualizer):
    def equalize(self, image, input_id):
        # 1) convert the color space to YCrCb and split the color channels
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        Y, Cb, Cr = cv2.split(image)

        # 2) equalize the Y channel and merge the channels
        equalized_y = self.histogram_equalization(Y)
        equalized_ycbcr_image = cv2.merge([equalized_y, Cb, Cr])

        # 3) convert back to BGR and save the image
        cv2.imwrite(f"image_{input_id}_{YCBCR_OUTPUT_PATH}", cv2.cvtColor(equalized_ycbcr_image, cv2.COLOR_YCrCb2BGR))
        print(SUCCESS_MSG)
