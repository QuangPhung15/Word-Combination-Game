from langdetect import detect
import os

def is_vietnamese(word):
    try:
        lang = detect(word)
        return lang == 'vi'
    except:
        return False


def rmSpecialChar(line):
    cleanStr = ""
    lastItem = ""
    symbols = [",", ".", ";"]
    for item in line:
        if (item.isalnum() or item.isspace()):
            cleanStr += item
        else:
            if (item in symbols):
                cleanStr += " " + item + " "

    
    return cleanStr


def cleanText(folderPath, fileName, j):
    symbols = [",", ".", ";"]
    file = open(os.path.join(folderPath, fileName), "r")

    line = file.readline()

    output = open(os.path.join("output", fileName), "w")
    cleanStr = ""

    while (line and j > 0):
        words = rmSpecialChar(line)
        words = line.split()

        i = 0
        while (i < len(words)):
            if (not words[i].isalpha() or not is_vietnamese(words[i]) or words[i] in symbols):
                words.pop(i)
                if (cleanStr):
                    output.write(cleanStr + "\n")
                    cleanStr = ""
            else:
                cleanStr += words[i] + " "
                i += 1

        line = file.readline()

        j -= 1

    output.close()
    file.close()
