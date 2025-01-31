import numpy as np
import cv2


# Constants
IMAGE_PATH = "Images/balcony.jpg"
GRAYSCALE_PATH = "Output/grayscale.jpg"
RESULT_PATH = "Output/output.jpg"
MAX_GRAY_VALUE = 255
NUMBER_OF_GRAY_VALUES = 256
ONE_SHADE_OF_GRAY_EXCEPTION = "Image only has one shade of gray, can't apply histogram equalization."
WRONG_INPUT_PATH_EXCEPTION = "Couldn't read the input image."
WRONG_NUMBER_EXCEPTION = "Invalid choice! Please select 1 for Grayscale, 2 for LAB, or 3 for HSV equalization."
INPUT_MSG = "Enter the number corresponding to your choice: "
EXIT_MSG = "Exiting the program..."
INVALID_MSG = "Invalid choice! Please select 1 for Grayscale, 2 for LAB, 3 for HSV, or 4 to Exit."
GRAYSCALE_EQUALIZATION_METHOD = "1"
LAB_EQUALIZATION_METHOD = "2"
HSV_EQUALIZATION_METHOD = "3"
EXIT_CHOICE = "4"


# Different histogram equalization functions
def histogram_equalization(image, gray=False):
    if gray:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 1) compute the cumulative image histogram
    hist, _ = np.histogram(image.flatten(), bins=NUMBER_OF_GRAY_VALUES, range=[0, NUMBER_OF_GRAY_VALUES])
    hist = np.cumsum(hist)

    # 2) normalize the cumulative histogram
    total_pixels = image.size
    hist = hist / total_pixels  # divide by total number of pixels

    non_zero_hist = np.nonzero(hist)
    min_gray  = np.min(non_zero_hist)  # first gray shade with >= 1 pixels
    min_value = hist[min_gray]
    max_gray = np.max(non_zero_hist)  # last gray shade with >= 1 pixels
    max_value = hist[max_gray]

    if min_value == max_value:
        raise Exception(ONE_SHADE_OF_GRAY_EXCEPTION)

    hist = MAX_GRAY_VALUE * ((hist - min_value) / (max_value - min_value))
    hist = np.round(hist).astype(np.uint8)

    # 3) map the intensity values of the image
    equalized_image = hist[image]

    return equalized_image


def apply_lab_equalization(image):
    # 1) convert to LAB color and split the channels
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_image)

    # 2) equalize the L channel and merge the channels
    equalized_l = histogram_equalization(l)
    equalized_lab_image = cv2.merge([equalized_l, a, b])

    # 3) convert back to BGR color and return
    return cv2.cvtColor(equalized_lab_image, cv2.COLOR_LAB2BGR)


def apply_hsv_equalization(image):
    # 1) convert to HSV color and split the channels
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    # 2) equalize the V channeland merge the channels
    equalized_v = histogram_equalization(v)
    equalized_hsv_image = cv2.merge([h, s, equalized_v])

    # 3) convert back to BGR color and return
    return cv2.cvtColor(equalized_hsv_image, cv2.COLOR_HSV2BGR)


def print_options():
    print("Choose the histogram equalization type:")
    print("1: Grayscale")
    print("2: LAB")
    print("3: HSV")
    print("4: Exit")

def main():
    # read image
    image = cv2.imread(IMAGE_PATH)
    if image is None:
        raise Exception(WRONG_INPUT_PATH_EXCEPTION)

    # ask the user for the type of equalization
    print_options()
    while True:
        choice = input(INPUT_MSG)
        if choice == GRAYSCALE_EQUALIZATION_METHOD:
            equalized_image = histogram_equalization(image, gray=True)
            break
        elif choice == LAB_EQUALIZATION_METHOD:
            equalized_image = apply_lab_equalization(image)
            break
        elif choice == HSV_EQUALIZATION_METHOD:
            equalized_image = apply_hsv_equalization(image)
            break
        elif choice == EXIT_CHOICE:
            print(EXIT_MSG)
            return  # Exit the program
        else:
            print(INVALID_MSG)

    # save result
    cv2.imwrite(RESULT_PATH, equalized_image)


if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)