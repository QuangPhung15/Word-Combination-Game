import re
import json
import math

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


def bigram_count(sentences):
    with open("Dictionary/wordsCount.json", "r") as f1:
        bigram_count = json.load(f1)

    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - 1):
          try:
            bigram_count[words[i]][words[i+1]] +=1
          except:
            pass
    with open("Dictionary/wordsCount.json", "w") as f2:
        json.dump(bigram_count, f2, indent=4, ensure_ascii=False)


def train_bigram_model():
    with open("Dictionary/wordsCount.json", "r") as f1:
        bigram_model = json.load(f1)
        bigram_count = bigram_model.copy()

        for w1 in bigram_count:
            count = sum(bigram_count[w1].values())
            for w2 in bigram_count[w1]:
                bigram_model[w1][w2] = bigram_count[w1][w2] / count 
            sorted_items = sorted(bigram_model[w1].items(), key=lambda x: x[1])
            sorted_dict = dict(sorted_items)
            bigram_model[w1] = sorted_dict


    with open("Dictionary/wordsProb.json", "w") as f2:
        json.dump(bigram_model, f2, indent=4, ensure_ascii=False)


def generate_next_word(tokens, beam = False):
    with open("Dictionary/wordsProb.json", "r") as f1:
        model = json.load(f1)
    probs_next = model[tokens]
    potentials = list(probs_next.keys())
    return potentials[0]

def generate_next_word_beam(tokens):
    with open("Dictionary/wordsProb.json", "r") as f1:
        model = json.load(f1)
    potentials = []
    probs_next = model[tokens]
    for next_word in probs_next:
        score1 = probs_next[next_word]
        scores = []
        probs_next_next = model[next_word]
        for next_next_word in probs_next_next:
            score2 = probs_next_next[next_next_word]
            score = score1 - math.log(score2)
            scores.append(score)
        scores.sort()
        potentials.append((scores[0], next_word))
    potentials.sort()
    return potentials[0]


