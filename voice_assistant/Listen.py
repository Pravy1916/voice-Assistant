import speech_recognition as sr
# from Speak import Say
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # Say("Listening")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing...")
        # Say("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")
    except:
        print("unrecognized")
        return "unrecognized"
    query = str(query)
    return query.lower()




