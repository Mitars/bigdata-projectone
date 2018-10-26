import sys


def printTitle(text):
    """Prints the title

    Arguments:
        text (string) -- The text to display in the title.
    """

    sys.stdout.write("\x1b]2;" + text + "\x07")


def printConsoleAndTitle(text):
    """Prints to the console and console title.

    Arguments:
        text (string) -- The text to display in the console and title.
    """

    sys.stdout.write("\x1b]2;" + text + "\x07")
    print(text)
