import speech_recognition as sr
from googletrans import Translator

# Initialize speech recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def recognize_and_translate():
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)

        print("Translating...")
        translated_text = translator.translate(text, dest='fr')
        print("Translation (to French):", translated_text.text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print("Error fetching results from Google Speech Recognition service:", e)

recognize_and_translate()
