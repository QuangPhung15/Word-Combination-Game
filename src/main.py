from clean import *
from gen_word import *
import os 
import extra_function as ef

ef.separateCorpus("vie_wikipedia_2021_1M-sentences")

for i in range(10):
    path = f"vie_wikipedia_2021_1M-sentences{i}.txt"
    cleanText("vie_wikipedia_2021_1M-sentences", path)

for i in range(10):
    path = f"vie_wikipedia_2021_1M-sentences{i}.txt"
    sentences = read_data(os.path.join("output", path))
    bigram_count(sentences)
    train_bigram_model()

# a = generate_next_word_beam('vãi')
# print(a)