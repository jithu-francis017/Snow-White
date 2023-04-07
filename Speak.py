import pyttsx3

def speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    engine.setProperty('language', 'en-in')
    engine.setProperty('gender', 'female')
    engine.setProperty('volume', 1)
    engine.setProperty('age', 'adult')
    engine.setProperty('rate', 178)
    print("    ")
    print(f"SnowWhite: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("     ")



#speak('Hello, Jithu')
