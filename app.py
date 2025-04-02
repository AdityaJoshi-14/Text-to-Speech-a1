from flask import Flask, request, send_file, render_template
from gtts import gTTS
import os

app = Flask(__name__)

# Serve the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Text-to-Speech API
@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get("text", "")
    lang = data.get("lang", "en")  # Default to English

    if not text:
        return {"error": "No text provided"}, 400

    try:
        # Generate speech with selected language
        tts = gTTS(text=text, lang=lang)
        filename = "output.mp3"
        tts.save(filename)
        
        return send_file(filename, as_attachment=True)
    
    except Exception as e:
        return {"error": str(e)}, 500  # Return error if something goes wrong

if __name__ == '__main__':
    app.run(debug=True)

