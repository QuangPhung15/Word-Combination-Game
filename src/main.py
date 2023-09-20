from clean import *
from gen_word import *
import os 

# cleanText("", "corpus.txt", 10)

# sentences = read_data(os.path.join("vie_wikipedia_2016_10K", "vie_wikipedia_2016_10K-sentences.txt"))
# sentences = read_data(os.path.join("output", "corpus.txt"))
# # print(sentences)


# model = train_bigram_model(sentences)
# # print(model)

# dictionary = generate_dict("vietnamese-syllables.txt")
# # print(dictionary)

# a = generate_next_word(model, dictionary, ["đòi", "tiền"])
# print(a)

makeVNWordDict()