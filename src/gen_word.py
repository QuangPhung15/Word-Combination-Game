import re

from collections import defaultdict


def read_data(corpus_file, num_sents=1e+6):
    sents = []
    count = 0
    for line in open(corpus_file, 'r', encoding='utf-8'):
        line = line.replace('\n', '').lower()
        words = re.findall(r'\w+', line)
        sentence = "<s> " + " ".join(words) + " </s>"
        sents.append(sentence)

        count += 1
        if count >= num_sents:
            break
    return sents


def train_bigram_model(sentences):
    bigram_model = defaultdict(lambda: defaultdict(int))
    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - 1):
            bigram_model[words[i]][words[i+1]] +=1
    
    for w1 in bigram_model:
        count = sum(bigram_model[w1].values())
        for w2 in bigram_model[w1]:
            bigram_model[w1][w2] = bigram_model[w1][w2] / count
    
    return bigram_model


def generate_dict(syllable_filename):
    viet_dict = []
    for word in open(syllable_filename).read().splitlines():
        viet_dict.append(word)
    return viet_dict


def generate_next_word(model, dict, tokens):
    potentials = []
    word = tokens[-1]
    probs_next = model[word]
    for next_word in probs_next:
        if next_word != '</s>' and next_word in dict:
            score = probs_next[next_word]
            potentials.append((score, next_word))
    potentials.sort()
    return potentials[0]
