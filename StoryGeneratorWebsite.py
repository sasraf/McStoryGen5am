import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
# from pymongo import MongoClient

from helperFunctions import *
from Main import *

# Configure MongoDB Client
# client = MongoClient("mongodb+srv://Sakib:<VdnPnbDAokF6yGtC>@storygenerator-qp5jo.mongodb.net/test?retryWrites=true&w=majority")
# db = client.words

# Configure App
app = Flask(__name__)

# App autoreloads
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    """Home page"""
    return render_template("homepage.html")

@app.route("/storyTime", methods=["GET"])
def storyGeneration():
    """Generate story, send to output"""
    if request.method == "GET":
        # generatedText = randomWords("time", 100)

        runTextGen()
        reader = open("textgenrnn_texts.txt","r")
        generatedText = reader.read()
        return render_template("storygen.html", outputText="Once upon a " + generatedText)

# @app.route("/installBooks", methods=["GET"])
# def installBooks():
#     """Install books"""

#     if request.method == "GET":

#         #TODO: MAKE THIS LESS BAD!!!!

#         # Read text from .txt file with books copied from
#         # Project gutenberg TODO: (replace in future with API call)
#         words = open("11-0.txt", "r")

#         # Tokenizes punctuation to make it easier to store punctuation in the markov chain
#         words = tokenizePunctuation(words)

#         # Tokenize string: https://www.geeksforgeeks.org/python-string-split/
#         tokenizedWords = words.split(' ')

#         # Converts all words to lowercase
#         tokenizedWords = decapitalizeWords(tokenizedWords)

#         # Initializes a list to store tokens in
#         uniqueWords = list()

#         # Making a new list with unique words
#         for tokenizedWord in tokenizedWords:

#             if tokenizedWord not in uniqueWords:
#                 uniqueWords.append(tokenizedWord)

#         # Compiling a list of following words per unique word; add to SQL database
#         for uniqueWord in uniqueWords:
#             # Find where uniqueWord == tokenizedWord, add the following word to a list
#             wordsForDatabase = list()
#             for num in range(len(tokenizedWords) - 1):
#                 if uniqueWord == tokenizedWords[num]:
#                     wordsForDatabase.append(tokenizedWords[num + 1])

#             condenser(wordsForDatabase, uniqueWord)
#         return render_template("homepage.html")







