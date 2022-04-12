# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr

r = sr.Recognizer()
wake_word = 'Wikipedia'

with sr.Microphone() as source:
    print("Ready!")
    audio = r.listen(source)

text = r.recognize_google(audio)
print(text)

if wake_word in text:
    print("Wake Word Detected!")
    text = text.replace(wake_word,"")
    print(text)
else:
    print("Wake Word Not Detected!")