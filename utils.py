import sys


# Console Colors
CONSOLE_HEADER = '\033[95m'
CONSOLE_OKBLUE = '\033[94m'
CONSOLE_OKGREEN = '\033[92m'
CONSOLE_WARNING = '\033[93m'
CONSOLE_FAIL = '\033[91m'
CONSOLE_ENDC = '\033[0m'
CONSOLE_BOLD = '\033[1m'
CONSOLE_UNDERLINE = '\033[4m'


def console_bold(text):
    """Formats the text with a console bold format.

    Args:
        text (string): The text to format

    Returns:
        string: The bolded text.
    """
    return CONSOLE_BOLD + text + CONSOLE_ENDC


def print_title(text):
    """Prints the title

    Arguments:
        text (string) -- The text to display in the title.
    """
    sys.stdout.write("\x1b]2;" + text + "\x07")


def print_console_and_title(text):
    """Prints to the console and console title.

    Arguments:
        text (string) -- The text to display in the console and title.
    """
    sys.stdout.write("\x1b]2;" + text + "\x07")
    print(text)
