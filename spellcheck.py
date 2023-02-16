# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])



    #menu
    menuloop = True
    while menuloop:
        print("\nMain Menu")
        print("1: Spell Check a Word (Linear Search)")
        print("2: Spell Check a Word (Binary Search)")
        print("3: Spell Check Alice In Wonderland (Linear Search)")
        print("4: Spell Check Alice In Wonderland (Binary Search)")
        print("5: EXIT")

        selection = input("please enter menu selection: ")

        #action
        if selection == "1":
            #linear dictionary
            word = input("Please enter a word: ")

            start = time.time()
            print("\nLinear Search starting...")

            check = linear_search(dictionary, word.lower())

            if check == -1:
                end = time.time()
                timeel = end - start
                print(f"{word} is NOT IN the dictionary. ({timeel} seconds)")
            else:
                end = time.time()
                timeel = end - start
                print(f"{word} is IN the dictionary at position {check}. ({timeel} seconds)")


        elif selection == "2":
            #binary dictionary
            word = input("Please enter a word: ")
            
            start = time.time()
            print("\nBinary Search starting...")

            check = binary_search(dictionary, word.lower())

            if check == -1:
                end = time.time()
                timeel = end - start
                print(f"{word} is NOT IN the dictionary. ({timeel} seconds)")
            else:
                end = time.time()
                timeel = end - start
                print(f"{word} is IN the dictionary at position {check}. ({timeel} seconds)")


        #alices

        elif selection == "3":
            #linear alice
            start = time.time()

            print("\nLinear Search starting...")
            notwords = 0

            for word in aliceWords:
                if linear_search(dictionary, word.lower()) == -1:
                    notwords += 1
            
            end = time.time()
            timeel = end - start
            print(f"Num of words not found in dictionary: {notwords} ({timeel} seconds)")


        elif selection == "4":
            #binary alice
            start = time.time()

            print("\nLinear Search starting...")
            notwords = 0

            for word in aliceWords:
                if binary_search(dictionary, word.lower()) == -1:
                    notwords += 1
            
            end = time.time()
            timeel = end - start
            print(f"Num of words not found in dictionary: {notwords} ({timeel} seconds)")



        elif selection == "5":
            print("\nEXIT")
            menuloop = False
        else:
            print("\nERR please enter a valid number")
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



#for each word in alice, I want to run search for that word in dictionary, then if found, cool good, if not -1 ++. Then move on to the next word