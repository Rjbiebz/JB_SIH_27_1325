import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
from speech_recognition import Recognizer

api_key= "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"

lang = ('en'
        'hi'
        'te')
openai.api_key = api_key
while true:
          def get_adio()
         r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

            if "hello" in said:
                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":said}])
                text = completion.choices[0].message.content
                speech = gTTS(text=text,lang=lang,slow=False,tld="com.au")
                speech.save("welcome1.mp3")
                playsound.playsound("welcome1.mp3")

        except Exception:
        print("Exception");

    return said

get_adio()

