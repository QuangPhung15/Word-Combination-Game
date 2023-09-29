import os
import json

def openVNWords():
    file = open("Dictionary/vnWords.json", "r")
    vnWords = json.load(file)

    return vnWords

def is_vietnamese(word, vnWords):
    try:
        vnWords[word]
        return True
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


def cleanText(folderPath, fileName):
    file = open(os.path.join("raw", folderPath, fileName), "r")
    output = open(os.path.join("output", fileName), "w")
    vnWords = openVNWords()

    symbols = [",", ".", ";"]

    line = file.readline()

    cleanStr = ""

    while (line):
        words = rmSpecialChar(line)
        words = words.split()

        i = 0
        while (i < len(words)):
            if ((not words[i].isalpha()) or (not is_vietnamese(words[i].lower(), vnWords) or (words[i] in symbols))):
                words.pop(i)
                if (cleanStr):
                    if (len(cleanStr.split()) != 1):
                        output.write(cleanStr + "\n")
                    cleanStr = ""
            else:
                cleanStr += words[i].lower() + " "
                i += 1

        line = file.readline()

    output.close()
    file.close()