from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters

params = PunktParameters()
ss = PunktSentenceTokenizer(params)


def print_split(text):
    out = [text[start:end] for start, end in ss.span_tokenize(text)]
    print(out)


print_split("He was a Ph.D.: that meant studying a lot.")

print_split("She is an M.D.: an oncologist. Please assist me.")

print_split("It was the Ph.D.'s responsibility to perform research.")

print_split("It was the M.D.'s responsibility to perform surgery.")
