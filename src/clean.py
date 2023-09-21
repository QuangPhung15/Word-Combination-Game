import os
import json

# def makeVNWordDict():
#     f = open("vietnamese-syllables.txt", "r")
#     vnDict = dict()

#     for word in f:
#         if word[0] not in vnDict:
#             vnDict[word[0]] = list()
#         vnDict[word[0]].append(word[1:len(word) - 1:1])

#     with open("VNWords.json", 'w') as json_file:
#         json.dump(vnDict, json_file)

def is_vietnamese(word):
    try:
        lang = detect(word)
        return lang == 'vi'
    except:
        return False


def rmSpecialChar(line):
    cleanStr = ""
    symbols = [",", ".", ";"]
    for item in line:
        if (item.isalnum() or item.isspace()):
            cleanStr += item
        else:
            if (item in symbols):
                cleanStr += " " + item + " "

    return cleanStr


def cleanText(folderPath, fileName, j):
    with open('VNWords.json', 'r') as json_file:
        vnWords = json.load(json_file)

    symbols = [",", ".", ";"]
    file = open(os.path.join(folderPath, fileName), "r")

    line = file.readline()

    output = open(os.path.join("output", fileName), "w")
    cleanStr = ""

    while (line and j > 0):
        words = rmSpecialChar(line)
        words = words.split()

        print(words)

        i = 0
        while (i < len(words)):
            if ((not words[i].isalpha()) or (not is_vietnamese(words[i])) or (words[i] in symbols)):
                words.pop(i)
                if (cleanStr):
                    if (len(cleanStr.split()) != 1):
                        print(cleanStr)
                        output.write(cleanStr + "\n")
                    cleanStr = ""
            else:
                cleanStr += words[i].lower() + " "
                i += 1

        line = file.readline()

        j -= 1

    output.close()
    file.close()