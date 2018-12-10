from data import DICTIONARY, LETTER_SCORES
import unittest
import test_wordvalue


def load_words(file=DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(file) as f:
        words = f.read().strip().split('\n')
        return words


def calc_word_value(word=""):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum((LETTER_SCORES[letter.upper()]for letter in word if letter.isalpha()))


def max_word_value(words=load_words(DICTIONARY)):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return sorted(words, key=calc_word_value)[-1]


if __name__ == "__main__":
    # run unittests to validate
    suite = unittest.TestLoader().loadTestsFromModule(test_wordvalue)
    unittest.TextTestRunner(verbosity=2).run(suite)
