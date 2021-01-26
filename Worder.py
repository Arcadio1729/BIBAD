import re
import os

class Worder:
    WorkingText=""

    def __init__(self, working_text=None):
        if working_text == None:
            self.WorkingText=""
        else:
            self.WorkingText = working_text

    def getTokens(self):
        return re.findall("\w+", self.WorkingText)

    def getSentences(self):
        return re.findall("[^.!?]*[.!?]", self.WorkingText)

    def getTextFromFile(self, path):
        file = open(path)
        self.WorkingText = file.read()  # ideą generatorów jest to, żeby nie wczytywać całego pliku
        file.close()


if __name__ == "__main__":
    w = Worder()
    w.getTextFromFile("nkjp.txt")
    print(w.WorkingText)