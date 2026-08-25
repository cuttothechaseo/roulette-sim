"""Practice moving one value between functions.

Complete the three TODOs in main(). Do not change the two helper functions.
"""


def choose_word():
    """Produce and return one value."""
    word = "python"
    return word


def count_letters(word):
    """Receive one value and return a new value."""
    letter_count = len(word)
    return letter_count


def main():
    # TODO 1: Call choose_word() and store its returned value in a variable
    # named chosen_word.
    chosen_word = choose_word()

    # TODO 2: Pass chosen_word to count_letters() and store its returned value
    # in a variable named number_of_letters.
    number_of_letters = count_letters(chosen_word)

    # TODO 3: Print chosen_word and number_of_letters.
    # Expected output: python 6
    print(chosen_word, number_of_letters)


if __name__ == "__main__":
    main()
