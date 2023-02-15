# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

#searches:
def linear_search(array, item):

    for x in range(len(array)):

        if array[x] == item:
            return x

    return -1

def binary_search(array, item):
    #index's
    li = 0
    ui= len(array)-1

    while li<=ui:
        #acquire middle index
        mi = (li+ui)//2

        #check
        if array[mi] == item:
            return mi

        elif array[mi] > item:
            ui = mi-1

        elif array[mi] < item:
            li = mi+1

    #n/a
    return -1


# Call main() to begin program
main()
