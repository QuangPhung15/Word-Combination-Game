from clean import *
from gen_word import *
import os 

cleanText("vie_wikipedia_2016_10K", "vie_wikipedia_2016_10K-sentences.txt", 1000)

# sentences = read_data(os.path.join("output", "vie_wikipedia_2016_10K-sentences.txt"))

# model = train_bigram_model(sentences)

# dictionary = generate_dict("vietnamese-syllables.txt")

# potentials = generate_next_word(model, dictionary, "mạnh")
