import json
import os
import zipfile

def zipFolder(folder):
    folder_to_zip = folder

    output_zip_file = f"{folder}.zip"

    with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_to_zip):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_to_zip)
                zipf.write(file_path, arcname=arcname)


def gen_vn_dict():
    with open("Dictionary/words.txt", "r") as f1, open("Dictionary/wordsProb.json", "w") as f2, open("Dictionary/wordsCount.json", "w") as f3:
        wordProb = {}
        wordCount = {}

        for line in f1:
            line = json.loads(line)
            word = line["text"]
            words = word.split(" ")
            size = len(words)

            if size == 2:
                if words[0].lower() not in wordProb:
                    wordProb[words[0].lower()] = {}
                    wordCount[words[0].lower()] = {}
                wordProb[words[0].lower()][words[1].lower()] = 0.0
                wordCount[words[0].lower()][words[1].lower()] = 1
        
        json.dump(wordProb, f2, indent=4, ensure_ascii=False)
        json.dump(wordCount, f3, indent=4, ensure_ascii=False)


def separateCorpus(file):
    try:
        os.mkdir(f"raw/{file}")
    except:
        pass

    with open(file + ".txt", "r") as f1:
        line = f1.readline()
        j = 0
        while (line):
            f2 = open(f"raw/{file}/{file}{j}.txt", "w")
            for i in range(100000):
                f2.write(line)
                if (line):
                    line = f1.readline()
                else:
                    break
            j += 1

def createVNWordsJSON():
    f1 = open("Dictionary/words.txt", "r")
    f2 = open("Dictionary/vnWords.json", "w")

    vnWords = dict()

    for line in f1:
        line = json.loads(line)
        word = line["text"]
        words = word.split(" ")
        for item in words:
            vnWords[item.lower()] = 1
    
    json.dump(vnWords, f2, indent=4, ensure_ascii=False)

    f1.close()
    f2.close()

# gen_vn_dict()
# zipFolder("output")