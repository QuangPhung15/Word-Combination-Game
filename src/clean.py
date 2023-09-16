from langdetect import detect

def is_vietnamese(word):
    try:
        lang = detect(word)
        return lang == 'vi'
    except:
        return False


def cleanWiki(filePath, j):
    file = open(filePath, "r")

    line = file.readline()

    while (line and j > 0):
        words = line.split()
        print(words)

        while (words[0].isdigit()):
            words.pop(0)

        i = 0
        while (i < len(words)):
            if (not words[i].isalpha()):
                words.pop(i)
            elif (not is_vietnamese(words[i])):
                words.pop(i)
            else:
                i += 1

        print(words)

        line = file.readline()

        j -= 1

    file.close()
