import random
import json
import os
import torch
from Brain import NeuralNet
from Neuralnetwork import bag_of_words , tokenize
from feautures import *
import pyautogui




#------------------------------------
Name = "Jarvis"
from Listen import Listen
# from Speak import Say
from Task import NonInputExecution
from Task import InputExecution


async def Main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    with open("intents.json", 'r') as json_data:
        intents = json.load(json_data)

    FILE = "trainData.pth"
    data = torch.load(FILE)


    input_size = data['input_size']
    hideen_size = data['hidden_size']
    output_size = data['output_size']
    all_words = data['all_words']
    tags = data['tags']
    model_state = data['model_state']

    model = NeuralNet(input_size,hideen_size,output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()


    sentence = Listen()
    result = str(sentence)
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    
    
    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    additional_messages = []  # List to store additional messages
    
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])
                
               

                # await Say(reply)  # Call the Speak function to say the reply

                # Append additional messages if returned by functions
                if "time" in reply or "date" in reply or "day" in reply or "joke" in reply :
                    result = NonInputExecution(reply)
                    if result is not None:
                        additional_messages.append(result) 
                elif "wikipedia" in reply  or "greetings" in reply or "hai" in reply  or "bye" in reply or "health" in reply or "identity" in reply or "personal" in reply or "activity" in reply or "insult" in reply or "exclaim" in reply or "google" in reply or "youtube" in reply or "whatsapp" in reply or "math" in reply or "songs" in reply or "laptop" in reply or "website" in reply or "voice type" in reply or "helping mode" in reply or "weather" in reply or "noanswer" in reply:
                    result = InputExecution(reply, result)
                
                    if result is not None:
                        additional_messages.append(result)
                
                elif "call" in reply:
                    contact_name = result.replace("call to", "").strip()
                    make_phone_call(contact_name)


#----------------------------------------Tools---------------------------------------
                
                elif "wifi" in tag:
                    wifi()
                elif "bluetooth" in tag:
                    bluetooth()
                elif "airoplane mode" in tag:
                    airoplanemode()
                elif "battery saver" in tag:
                    batterysaver()
                elif "accessibility" in tag:
                    accessibility()
                elif "nearby sharing" in tag:
                    nearbysharing()
                elif "cast" in tag:
                    cast()
                elif "night light" in tag:
                    nightlight()
                elif "hotspot" in tag:
                    hotspot()
                elif "project" in tag:
                    project()

#-----------------------------------------shortcuts--------------------------------------------------------   

            #volume related
                elif "volume up" in tag:
                    pyautogui.hotkey('volumeup')
                    
                elif "volume down" in tag:
                    pyautogui.hotkey('volumedown')
                elif "mute volume" in tag:
                    pyautogui.hotkey('volumemute')
            
            #tabs related
                elif "new tab" in tag:
                    pyautogui.hotkey('ctrl','t')
                elif "close tab" in tag:
                    pyautogui.hotkey('ctrl','w')
                elif "recent tab" in tag:
                    pyautogui.hotkey('ctrl','shift','t')

            #windows related
                elif "screenshot" in tag:
                    pyautogui.hotkey('win','prtsc')
                elif "snippet" in tag:
                    pyautogui.hotkey('prtsc')

                elif "minimise windows" in tag:
                    pyautogui.hotkey('win','d')
                elif "window left" in tag:
                    pyautogui.hotkey('win','left')
                elif "window right" in tag:
                    pyautogui.hotkey('win','right')
                elif "window up" in tag:
                    pyautogui.hotkey('win','up')
                elif "window down" in tag:
                    pyautogui.hotkey('win','down')
                elif "notification bar" in tag:
                    pyautogui.hotkey('win','n')
                

            #desktop realated
                elif "create desktop" in tag:
                    pyautogui.hotkey('ctrl','win','d')
            
                elif "right desktop" in tag:
                    pyautogui.hotkey('ctrl','win','right')
            
                elif "left desktop" in tag:
                    pyautogui.hotkey('ctrl','win','left')
            
                elif "delete desktop" in tag:
                    pyautogui.hotkey('ctrl','win','f4')
            
            #power related
                elif "restart" in tag:
                    os.system("shutdown /r /f /t 5")
                
                elif "shutdown" in tag:
                    os.system("shutdown /s /f /t 5")


                return reply, additional_messages
    else:           
        return "Sorry!, Your are not matched with us ",[]    
                
            


# def Main():
#     sentence = Listen()
#     result = str(sentence)
#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence,all_words)
#     X = X.reshape(1,X.shape[0])
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
#     _ , predicted = torch.max(output,dim=1)
#     tag = tags[predicted.item()]
#     probs = torch.softmax(output,dim=1)
#     prob = probs[0][predicted.item()]

#     if prob.item() > 0.75:
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 reply = random.choice(intent["responses"])
#                 Say(reply)
#                 print(reply)

        
#                 if "bye" in tag:
#                     exit()

#                 elif "time" in reply:                   
#                     NonInputExecution(reply)

#                 elif "date" in reply:                   
#                     NonInputExecution(reply)

#                 elif "day" in reply:
#                     NonInputExecution(reply)

#                 elif "joke" in reply:
#                     NonInputExecution(reply)
                
#                 elif "wikipedia" in reply:
#                     InputExecution(reply,result)
            
#                 elif "greetings" in reply:
#                     InputExecution(reply,result)
                
#                 elif "google" in reply:
#                     InputExecution(reply,result)

#                 elif "youtube" in reply:
#                     InputExecution(reply,result)
            
#                 elif "call" in reply:
#                     contact_name = result.replace("call to", "").strip()
#                     make_phone_call(contact_name)

#                 elif "whatsapp" in reply:
#                     InputExecution(reply,result)

#                 elif "math" in reply:
#                     InputExecution(reply,result)
#                 elif "songs" in reply:
#                     InputExecution(reply,result)
                

# # ------------------------------------helping mode---------------------------------------------------
                
#                 elif "helping mode" in tag:
#                     helping()

# # --------------------------installed applications-----------------------------------------------
#                 elif "laptop" in reply:
#                     InputExecution(reply,result)
# # --------------------------------websites----------------------------------------------

#                 elif "website" in reply:
#                     InputExecution(reply,result)

# # --------------------------------TOOLS----------------------------------------------------------

#                 elif "wifi" in tag:
#                     wifi()
#                 elif "bluetooth" in tag:
#                     bluetooth()
#                 elif "airoplane mode" in tag:
#                     airoplanemode()
#                 elif "battery saver" in tag:
#                     batterysaver()
#                 elif "accessibility" in tag:
#                     accessibility()
#                 elif "nearby sharing" in tag:
#                     nearbysharing()
#                 elif "cast" in tag:
#                     cast()
#                 elif "night light" in tag:
#                     nightlight()
#                 elif "hotspot" in tag:
#                     hotspot()
#                 elif "project" in tag:
#                     project()

# #-----------------------------------------shortcuts--------------------------------------------------------   
#             #volume related
#                 elif "volume up" in tag:
#                     pyautogui.hotkey('volumeup')
#                 elif "volume down" in tag:
#                     pyautogui.hotkey('volumedown')
#                 elif "mute volume" in tag:
#                     pyautogui.hotkey('volumemute')
            
#             #tabs related
#                 elif "new tab" in tag:
#                     pyautogui.hotkey('ctrl','t')
#                 elif "close tab" in tag:
#                     pyautogui.hotkey('ctrl','w')
#                 elif "recent tab" in tag:
#                     pyautogui.hotkey('ctrl','shift','t')

#             #windows related
#                 elif "screenshot" in tag:
#                     pyautogui.hotkey('win','prtsc')
#                 elif "snippet" in tag:
#                     pyautogui.hotkey('prtsc')

#                 elif "minimise windows" in tag:
#                     pyautogui.hotkey('win','d')
#                 elif "window left" in tag:
#                     pyautogui.hotkey('win','left')
#                 elif "window right" in tag:
#                     pyautogui.hotkey('win','right')
#                 elif "window up" in tag:
#                     pyautogui.hotkey('win','up')
#                 elif "window down" in tag:
#                     pyautogui.hotkey('win','down')
#                 elif "notification bar" in tag:
#                     pyautogui.hotkey('win','n')

#             #desktop realated
#                 elif "create desktop" in tag:
#                     pyautogui.hotkey('ctrl','win','d')
            
#                 elif "right desktop" in tag:
#                     pyautogui.hotkey('ctrl','win','right')
            
#                 elif "left desktop" in tag:
#                     pyautogui.hotkey('ctrl','win','left')
            
#                 elif "delete desktop" in tag:
#                     pyautogui.hotkey('ctrl','win','f4')
            
#             #power related
#                 elif "restart" in tag:
#                     os.system("shutdown /r /f /t 5")
                
#                 elif "shutdown" in tag:
#                     os.system("shutdown /s /f /t 5")

# #------------------------------- vice type ----------------------------------------------
#                 elif "voice type" in reply:
#                     InputExecution(reply,result)
    