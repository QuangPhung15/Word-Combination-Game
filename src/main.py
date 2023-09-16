from clean import *
from gen_word import *
import os 

cleanText("vie_wikipedia_2016_10K", "vie_wikipedia_2016_10K-sentences.txt", 10000)

# sentences = read_data(os.path.join("output", "vie_wikipedia_2016_10K-sentences.txt"))
# print(sentences)
# model = train_bigram_model(sentences)

# dictionary = generate_dict("vietnamese-syllables.txt")

# generate_next_word(model, dictionary, "là")
