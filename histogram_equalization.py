import os
os.environ["OPENCV_LOG_LEVEL"]="SILENT"
import cv2
import equalizer_factory


# Constants
# String messages
GREET_USER = "Hello :)"
PROVIDE_INPUT_PATH = "Please provide the path to the image you want to use. \n "
WRONG_INPUT_PATH_EXCEPTION = "Couldn't read the input image. Please make sure that the path given is correct."
EXIT_MSG = "Exiting the program..."
INVALID_CONTINUE_MSG = "Invalid choice! \nPlease select 1 to continue, 2 to exit."
INVALID_CHANGE_IMAGE_MSG = "Invalid choice! \nPlease select 1 to load a new image, 2 to use the current one."
DESIRE_TO_CHANGE_IMAGE = "Would you like to load a new picture or use the current one?"
CHANGE_IMAGE_OPTIONS = "1: Use another picture \n2: Use the current picture"
DESIRE_TO_CONTINUE = "Would you like to use a different color space / image?"
CONTINUE_OPTIONS = "1: Yes \n2: No"

# Variables
CONTINUE = "1"
FINISH = "2"
CONTINUE_WORK = False
FINISH_WORK = True
USE_DIFFERENT_IMAGE = "1"
USE_SAME_IMAGE = "2"
NO_NEED_TO_LOAD_IMAGE = False
SHOULD_LOAD_IMAGE = True


# Helper function
def ask_if_user_wants_to_use_another_image():
    print(DESIRE_TO_CHANGE_IMAGE)
    print(CHANGE_IMAGE_OPTIONS)
    while True:
        choice = input()
        match choice:
            case _ if choice == USE_DIFFERENT_IMAGE:
                return CONTINUE_WORK, SHOULD_LOAD_IMAGE

            case _ if choice == USE_SAME_IMAGE:
                return CONTINUE_WORK, NO_NEED_TO_LOAD_IMAGE

            case _:
                print(INVALID_CHANGE_IMAGE_MSG)


def ask_if_user_wants_to_continue():
    print(DESIRE_TO_CONTINUE)
    print(CONTINUE_OPTIONS)
    while True:
        choice = input()
        match choice:
            case _ if choice == CONTINUE:
                return ask_if_user_wants_to_use_another_image()

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
        return FINISH_WORK
    equalizer.equalize(image, input_id)
    return ask_if_user_wants_to_continue()


if __name__ == "__main__":
    try:
        print(GREET_USER)
        should_load_image, finished = True, False
        image, input_id = None, 0
        while not finished:
            if should_load_image:
                image = select_image()
                input_id += 1
            finished, should_load_image = main(image, input_id)
    except Exception as exception:
        print(exception)