from clean import *
from gen_word import *
import os 


# for i in range(95):
#     path = f"corpus{i}.txt"
#     cleanText("corpus", path)

# cleanText("vie_wikipedia_2016_10K", "vie_wikipedia_2016_10K-sentences.txt")

# for i in range(95):
#     path = f"corpus{i}.txt"
#     sentences = read_data(os.path.join("output", path))
#     bigram_count(sentences)
#     train_bigram_model()

a = generate_next_word_beam('vãi')
print(a)