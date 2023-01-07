from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench/<textToTranslate>")
def englishToFrench(textToTranslate):
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish/<textToTranslate>")
def frenchToEnglish(textToTranslate):
    return translator.french_to_english(textToTranslate)

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return "Something"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
