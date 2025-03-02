import cv2
import equalizer_factory


# Constants
# String messages
WRONG_INPUT_PATH_EXCEPTION = "Couldn't read the input image."
EXIT_MSG = "Exiting the program..."
SUCCESS_MSG = "Successfully created the desired output image."
INVALID_MSG = "Invalid choice! \nPlease select 1 to continue, 2 to exit."
DESIRE_TO_CONTINUE = "Would you like to use another histogram equalization method?"
DESIRE_OPTIONS = "1: Yes \n2: No"

# Variables
CONTINUE = "1"
FINISH = "2"
CONTINUE_WORK = False
FINISH_WORK = True

# Paths
IMAGE_PATH = "input.jpg"
GRAYSCALE_RESULT_PATH = "grayscale_output.jpg"


# Helper function
def ask_if_user_wants_to_continue():
    print(DESIRE_TO_CONTINUE)
    print(DESIRE_OPTIONS)
    while True:
        choice = input()
        match choice:
            case _ if choice == CONTINUE:
                return CONTINUE_WORK
            case _ if choice == FINISH:
                print(EXIT_MSG)
                return FINISH_WORK
            case _:
                print(INVALID_MSG)


# Main function
def main():
    image = cv2.imread(IMAGE_PATH)
    if image is None:
        raise Exception(WRONG_INPUT_PATH_EXCEPTION)
    equalizer = equalizer_factory.create_histogram_equalizer()
    if not equalizer:
        return FINISH_WORK
    equalizer.equalize(image)
    print(SUCCESS_MSG)
    return ask_if_user_wants_to_continue()


if __name__ == "__main__":
    try:
        finished = False
        while not finished:
            finished = main()
    except Exception as exception:
        print(exception)