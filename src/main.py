from clean import *
from gen_word import *
import os 


# for i in range(95):
#     path = f"corpus{i}.txt"
#     cleanText("corpus", path)

# cleanText("vie_wikipedia_2016_10K", "vie_wikipedia_2016_10K-sentences.txt")


# sentences = read_data(os.path.join("output", "corpus0.txt"))
# # print(sentences)


# model = train_bigram_model(sentences)
# # print(model)

# # dictionary = generate_dict("vietnamese-syllables.txt")
# # print(dictionary)

# a = generate_next_word(model, "đi")
# print(a)

# for i in range(95):
#     path = f"corpus{i}.txt"
#     sentences = read_data(os.path.join("output", path))
#     bigram_count(sentences)
#     train_bigram_model()
#     # a = generate_next_word('giới')
#     # print(a)

# train_bigram_model()
a = generate_next_word('mẹ')
print(a)