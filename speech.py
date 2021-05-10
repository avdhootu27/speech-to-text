import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything")
    audio = r.record(source,duration=5)

    try:
        text = r.recognize_google(audio)
        print("I heard : {}".format(text))
    except:
        print("Could not recognize your voice")
