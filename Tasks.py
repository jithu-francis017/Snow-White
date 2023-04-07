import datetime
import os
import wikipedia
import pywhatkit
from Speak import speak



def NonInputExecution(query):

    query = str(query)
    if "time" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(time)
    elif "date" in query:
        date = datetime.date.today()
        speak(date)

def InputExecution(tag, query):

    if "wikipedia" in tag:
        search_item = str(query).replace("who is","").replace("about","").replace("tell me about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(search_item)
        speak(result)
    elif "google" in tag:
        search_item = str(query).replace("google","").replace("search","").replace("google search","").replace("what is","")
        pywhatkit.search(search_item)