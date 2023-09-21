from clean import *
from gen_word import *
import os 


for i in range(94, 95):
    path = f"corpus{i}.txt"
    cleanText("corpus", path)


# sentences = read_data(os.path.join("output", "corpus.txt"))
# # print(sentences)


# model = train_bigram_model(sentences)
# # print(model)

# dictionary = generate_dict("vietnamese-syllables.txt")
# # print(dictionary)

# a = generate_next_word(model, dictionary, ["đòi", "tiền"])
# print(a)

