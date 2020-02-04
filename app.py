import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session

from textgenrnn import textgenrnn

# Configure App
app = Flask(__name__)

textgen = textgenrnn(weights_path='Test3_weights.hdf5',
                     vocab_path='Test3_vocab.json',
                     config_path='Test3_config.json')

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
        open('textgenrnn_texts.txt', 'w').close()
        textgen.generate_samples(max_gen_length=1000)
        textgen.generate_to_file('textgenrnn_texts.txt', max_gen_length=1000)
        reader = open("textgenrnn_texts.txt","r")
        generatedText = reader.read()
        return render_template("storygen.html", outputText=generatedText)
