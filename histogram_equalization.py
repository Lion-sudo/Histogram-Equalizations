import os
os.environ["OPENCV_LOG_LEVEL"]="SILENT"
import cv2
import equalizer_factory


# Constants
# String messages
GREET_USER = "Hello! Welcome to the Histogram Equalization Program."
PROVIDE_INPUT_PATH = "\nPlease provide the path to the image you want to use: \n"
WRONG_INPUT_PATH_EXCEPTION = "Error: Couldn't read the image. Please check the path and try again."
EXIT_MSG = "\nExiting the program... Goodbye!"
INVALID_CONTINUE_MSG = ("\nInvalid choice! \nPlease select 1 to continue using the current image, "
                        "2 to load a new image, 3 to exit the program.")
DESIRE_TO_CONTINUE = "\nWould you like to continue or exit?"
CONTINUE_OPTIONS = "1: Continue using the current image \n2: Load a new image \n3: Exit the program"
CONTINUE_INPUT_MSG = "Enter the number corresponding to your choice: "

# Variables
CONTINUE_CURRENT_IMAGE = "1"
CONTINUE_USING_DIFFERENT_IMAGE = "2"
FINISH = "3"
CONTINUE_WORK = False
FINISH_WORK = True
NO_NEED_TO_LOAD_IMAGE = False
SHOULD_LOAD_IMAGE = True


# Helper function
def ask_if_user_wants_to_continue():
    print(DESIRE_TO_CONTINUE)
    print(CONTINUE_OPTIONS)
    while True:
        choice = input(CONTINUE_INPUT_MSG)
        match choice:
            case _ if choice == CONTINUE_CURRENT_IMAGE:
                return CONTINUE_WORK, NO_NEED_TO_LOAD_IMAGE

            case _ if choice == CONTINUE_USING_DIFFERENT_IMAGE:
                return CONTINUE_WORK, SHOULD_LOAD_IMAGE

            case _ if choice == FINISH:
                print(EXIT_MSG)
                return FINISH_WORK, NO_NEED_TO_LOAD_IMAGE

            case _:
                print(INVALID_CONTINUE_MSG)


def select_image():
    path = input(PROVIDE_INPUT_PATH)
    image = cv2.imread(path)
    if image is None:
        raise Exception(WRONG_INPUT_PATH_EXCEPTION)
    return image


# Main function
def main(image, input_id):
    equalizer = equalizer_factory.create_histogram_equalizer()
    if not equalizer:
        return FINISH_WORK, NO_NEED_TO_LOAD_IMAGE
    equalizer.equalize(image, input_id)
    return ask_if_user_wants_to_continue()


if __name__ == "__main__":
    try:
        print(GREET_USER, end="")
        should_load_image, finished = True, False
        image, input_id = None, 0
        while not finished:
            if should_load_image:
                image = select_image()
                input_id += 1
            finished, should_load_image = main(image, input_id)
    except Exception as exception:
        print(exception)