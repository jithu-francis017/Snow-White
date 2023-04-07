import speech_recognition as sr
#import noisereduce as nr

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("     ")
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
        
    
    try:
        print("Recognizing...")
        #audio = nr.reduce_noise(audio.get_wav_data(), audio.sample_rate)
        response = r.recognize_google(audio, language="en-in", show_all=True)
        query = response['alternative'][0]['transcript']
        print(f"You Said: {query}")
        print("     ")

    except:
        return ""
    
    query = str(query)
    return query.lower()

