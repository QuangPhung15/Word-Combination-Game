import json
import os

def gen_vn_dict():
    with open("Dictionary/words.txt", "r") as f1, open("Dictionary/words.json", "w") as f2:
        wordProb = {}

        for line in f1:
            line = json.loads(line)
            word = line["text"]
            words = word.split(" ")
            size = len(words)

            if size == 2:
                if words[0].lower() not in wordProb:
                    wordProb[words[0].lower()] = {}
                wordProb[words[0].lower()][words[1].lower()] = 0.0
        
        json.dump(wordProb, f2, indent=4)

def separateCorpus(file):
    try:
        os.mkdir(file)
    except:
        pass

    with open(file + ".txt", "r") as f1:
        line = f1.readline()
        j = 0
        while (line):
            f2 = open(f"{file}/{file}{j}.txt", "w")
            for i in range(100000):
                f2.write(line)
                if (line):
                    line = f1.readline()
                else:
                    break
            j += 1
