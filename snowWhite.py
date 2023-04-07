import random
import json
import torch
import numpy as np
from Brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("intents.json","r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#-------------------------
Name = "Snow White"

from Listen import Listen
from Speak import speak
from Tasks import NonInputExecution, InputExecution

def Main():
    sentence = Listen()
    result = str(sentence)

    if sentence == "bye":
        exit()

    sentence = tokenize(sentence)
    x = bag_of_words(sentence,all_words)
    x = x.reshape(1,x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                replay = random.choice(intent["responses"])

                if "time" in replay:
                    NonInputExecution(replay)
                elif "date" in replay:
                    NonInputExecution(replay)
                elif "wikipedia" in replay:
                    InputExecution(replay,result)
                elif "google" in replay:
                    InputExecution(replay,result)
                else:
                    speak(replay)

while True:
    Main()