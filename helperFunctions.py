from random import randint

from flask import redirect, render_template, request, session
# from pymongo import MongoClient

import re

# Configure MongoDB Client
# client = MongoClient("mongodb+srv://Sakib:<VdnPnbDAokF6yGtC>@storygenerator-qp5jo.mongodb.net/test?retryWrites=true&w=majority")
# db = client.words

# def randomWords(startingWord, numberOfWords):
#     """Returns randomly generated text depending on the starting word"""

#     # Create a list of possible words using a startingWord
#     possibleWords = decondenser(startingWord)

#     # Initialize outputString as an empty string
#     outputString = ""

#     # Pick a random word from the decondensed list
#     # Random number generator: https://pythonspot.com/random-numbers/
#     for num in range(numberOfWords):

#         # Chooses a random number from 0 to the 0-indexed size of the list
#         randomNumber = randint(0, len(possibleWords) - 1)

#         # Picks a word in the list randomly using the random number
#         thisWord = possibleWords[randomNumber]

#         # Doesn't make a space before if the "word" is a punctuation mark
#         if (thisWord == "." or thisWord == "," or thisWord == "!" or thisWord == "?"):
#             outputString = outputString + thisWord
#         else:
#             outputString = outputString + " " + thisWord

#         # Get a list of possible words for the newly generated word
#         possibleWords = decondenser(possibleWords[randomNumber])

#     return outputString

# def decondenser(word):
#     """Takes the condensed text and decondenses it into a list"""
#     text = db.words.find_one({'keyWord': word})
#     tokenized = text[0]['next'].split('§')

#     # If no next word is found, return a conjunctioin instead
#     if(text[0]['next'] == ''):
#         return getConjunction()
#     else:
#         return tokenized

def getConjunction():
    """Returns a conjunction to be used when a word doesn't have a next word in the database"""
    conjunctions = ['and', 'but', 'yet', 'also']
    return conjunctions

def tokenizeChar(words, wordToTokenize):
    """Tokenizes puncutation by ensuring that there is a space before and after each punctuation symbol"""
    words = words.replace(wordToTokenize, " " + wordToTokenize + " ")
    return words

def tokenizePunctuation(words):
    """Tokenizes a string, returns the tokenized and cleaned up string"""
    # New lines are removed to reduce risk of error
    words = words.replace('\n', ' ')

    # Certain punctuation is tokenized to be added
    # into our database
    toTokenize = ",.!?"
    for c in toTokenize:
        words = tokenizeChar(words, c)

    # Certain punctuation marks (that are difficult to properly
    # implement) are removed for the time being.
    toRemove = "()\"{}[]"
    for c in toRemove:
        words = words.replace(c, '')

    # Removing extra spaces from string to keep the words.split in
    # application.py working properly
    # From: https://stackoverflow.com/questions/42357021/how-to-remove-extra-spaces-in-a-string
    words = re.sub(r' +', ' ', words)

    return words

def decapitalizeWords(tokenized):
    """Decapitalize all strings in a list"""
    for num in range(len(tokenized) - 1):
        # Check if a string is upper: https://stackoverflow.com/questions/8222855/check-if-string-is-upper-lower-or-mixed-case-in-python
        if tokenized[num].isupper():
            # Convert a string to lower: https://stackoverflow.com/questions/6797984/how-to-lowercase-a-string-in-python
            tokenized[num] = tokenized[num].lower()
    return tokenized

# def condenser(thisList, keyWord):
#     """Turn a list into a large string to be inputted in the database as text"""

#     # Initializing a string
#     reallyBigString = ''

#     for word in thisList:
#         reallyBigString = reallyBigString + "§" + word

#     # check if the word is already in the database; if it is then decondense what is already in the database
#     # then add reallybigstring to it, and insert it back in
#     # if it does not already exist, then make a new row in the database
#     thisWord = db.words.find_one({'keyWord': word})

#     if not thisWord:
#         # oldReallyBigString = db.words.find_one
#         db.words.insert_one({'keyWord': word}, {'next': reallyBigString})
#     else:
#         oldWords = db.words.find_one({'keyWord': thisWord})

#         newWords = str(reallyBigString + oldWords[0]['next'])

#         db.update_one({'keyWord': word}, {'next': newWords})