# Import all the equalizers
from EqualizerClasses.grayscale_histogram_equalizer import GrayscaleHistogramEqualizer
from EqualizerClasses.lab_histogram_equalizer import LabHistogramEqualizer
from EqualizerClasses.hsv_histogram_equalizer import HsvHistogramEqualizer
from EqualizerClasses.ycbcr_histogram_equalizer import YCBCRHistogramEqualizer
from EqualizerClasses.hsl_histogram_equalizer import HSLHistogramEqualizer


# Constants
# String messages
INSTRUCTIONS = "\nChoose the histogram equalization color space:"
OPTIONS = "1: Grayscale \n2: LAB \n3: HSV \n4: YCbCr \n5: HSL \n6: Exit"
INPUT_MSG = "Enter the number corresponding to your choice: "
INVALID_MSG = ("Invalid choice! \n"
               "Please select 1 for Grayscale, 2 for LAB, 3 for HSV, 4 for YCbCr, 5 for HSL "
               "or 6 to exit.")
EXIT_MSG = "Exiting the program..."

# Codes
GRAYSCALE_EQUALIZATION_METHOD = "1"
LAB_EQUALIZATION_METHOD = "2"
HSV_EQUALIZATION_METHOD = "3"
YCBCR_EQUALIZATION_METHOD = "4"
HSL_EQUALIZATION_METHOD = "5"
EXIT_CHOICE = "6"


def print_options():
    print(INSTRUCTIONS)
    print(OPTIONS)


def create_histogram_equalizer():
    while True:
        print_options()
        choice = input(INPUT_MSG)
        match choice:
            case _ if choice == GRAYSCALE_EQUALIZATION_METHOD:
                return GrayscaleHistogramEqualizer()

            case _ if choice == LAB_EQUALIZATION_METHOD:
                return LabHistogramEqualizer()

            case _ if choice == HSV_EQUALIZATION_METHOD:
                return HsvHistogramEqualizer()

            case _ if choice == YCBCR_EQUALIZATION_METHOD:
                return YCBCRHistogramEqualizer()

            case _ if choice == HSL_EQUALIZATION_METHOD:
                return HSLHistogramEqualizer()

            case _ if choice == EXIT_CHOICE:
                print(EXIT_MSG)
                return None

            case _:
                print(INVALID_MSG)