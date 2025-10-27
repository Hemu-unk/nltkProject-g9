import unittest
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

# Initialize the tokenizer
params = PunktParameters()
ss = PunktSentenceTokenizer(params)

def split_sentences(text):
    """Return a list of sentences from text using PunktSentenceTokenizer."""
    return [text[start:end] for start, end in ss.span_tokenize(text)]

# Unit tests
class TestSentenceSplitting(unittest.TestCase):

    def test_phd_sentence(self):
        text = "He was a Ph.D.: that meant studying a lot."
        expected = ["He was a Ph.D.: that meant studying a lot."]
        self.assertEqual(split_sentences(text), expected)

    def test_md_sentence(self):
        text = "She is an M.D.: an oncologist. Please assist me."
        expected = ["She is an M.D.: an oncologist.", "Please assist me."]
        self.assertEqual(split_sentences(text), expected)

    def test_phd_possessive(self):
        text = "It was the Ph.D.'s responsibility to perform research."
        expected = ["It was the Ph.D.'s responsibility to perform research."]
        self.assertEqual(split_sentences(text), expected)

    def test_md_possessive(self):
        text = "It was the M.D.'s responsibility to perform surgery."
        expected = ["It was the M.D.'s responsibility to perform surgery."]
        self.assertEqual(split_sentences(text), expected)

if __name__ == "__main__":
    unittest.main()

#def print_split(text):
    #out = [text[start:end] for start, end in ss.span_tokenize(text)]
    #print(out)

#print_split("He was a Ph.D.: that meant studying a lot.")
#print_split("She is an M.D.: an oncologist. Please assist me.")
#print_split("It was the Ph.D.'s responsibility to perform research.")
#print_split("It was the M.D.'s responsibility to perform surgery.")

