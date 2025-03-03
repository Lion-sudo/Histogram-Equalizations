import cv2
from EqualizerClasses.abstract_histogram_equalizer import  AbstractHistogramEqualizer


# Constants
LAB_RESULT_PATH = "lab_output.jpg"
SUCCESS_MSG = "Finished LAB histogram equalization successfully."


class LabHistogramEqualizer(AbstractHistogramEqualizer):
    def equalize(self, image, input_id):
        # 1) convert to LAB color and split the channels
        lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab_image)

        # 2) equalize the L (Lightness) channel and merge the channels
        equalized_l = self.histogram_equalization(l)
        equalized_lab_image = cv2.merge([equalized_l, a, b])

        # 3) convert back to BGR color and save the image
        cv2.imwrite(f"image_{input_id}_{LAB_RESULT_PATH}", cv2.cvtColor(equalized_lab_image, cv2.COLOR_LAB2BGR))
        print(SUCCESS_MSG)