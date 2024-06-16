
from time import sleep
from Listen import Listen
# from Speak import Say
import pyautogui
from pywikihow import search_wikihow 
import requests
from Speak import Say
import datetime

#------------------------------------------tools----------------------------------
def wifi():
    pyautogui.click(x=1721, y=1049)
    sleep(1)
    pyautogui.click(x=1576, y=329)
    sleep(1)
    pyautogui.click(x=1858, y=306)


def bluetooth():
    pyautogui.click(x=1721, y=1049)
    sleep(1)
    pyautogui.click(x=1699, y=334)
    sleep(1)
    pyautogui.click(x=1847, y=302)

def airoplanemode():
    pyautogui.click(x=1721, y=1049)
    sleep(1)
    pyautogui.click(x=1818, y=344)


def batterysaver():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1528, y=468)

def accessibility():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1676, y=461)

def nearbysharing():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1805, y=466)

def cast():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1563, y=566)

def nightlight():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1693, y=571)

def hotspot():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1808, y=577)

def project():
  pyautogui.click(x=1721, y=1049)
  sleep(1)
  pyautogui.click(x=1525, y=695)

#--------------------------------------------voice type--------------------------------------

def VoiceType():
   Say("voice type started! make sure your cursor must be in any search area")
   while True:
    query = Listen()
    if query == "stop voice type":
      # Say("Voice typing stopped.")
      return "Voice typing stopped."
      # exit()
    else:
      pyautogui.write(" "+query)

#--------------------------------------helping mode---------------------------------------

# def helping():
#     # Say("say! how can i help you today")
#     how=Listen()
#     max_result=1
#     how_to=search_wikihow(how,max_result)
#     assert len(how_to)==1
#     print(how_to[0])
#     # Say(how_to[0].summary)
#     return how_to[0].summary

#------------------------------------call--------------------------------------------

def make_phone_call(contact_name):
    try:
        import time
        import pyautogui
        search_url = f"tel:"
        import webbrowser
        # Open the URL in the default web browser
        webbrowser.open(search_url)
        time.sleep(8)
        pyautogui.click(x=1722, y=181)
        time.sleep(1)
        pyautogui.write(contact_name)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=1666, y=881)
        pyautogui.press('enter')
    except Exception as e:
        print(f"Error initiating phone search: {e}")
        return f"Error initiating phone search: {e}"


# ----------------------------------weather-------------------------------------------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(query):
    query = query.replace("weather", "")
    query = query.replace("today", "")
    query = query.replace("now", "")
    query = query.replace("of", "")
    query = query.replace("in", "")

    if query == "":
        city = "narasaraopet" + " weather"
    else:
        city = query+" weather"

    try:

        url = "https://weatherapi-com.p.rapidapi.com/current.json"

        querystring = {"q": city}

        headers = {
            "X-RapidAPI-Key": "d68c7a4ca0mshfe7db0559a72ad6p1f118fjsnb3beeaa77aac",
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        weather = response.json()['current']['feelslike_c']
        info = response.json()['current']['wind_kph']
        return  "its "+str(weather)+" degree celsius and wind speed is "+str(weather)+" kilometer per hour in "+city
        
    except IndexError:
        return "Can't found city " + query
# ---------------------------------------wishes-------------------------------------------------
def wishes():
  current_hour = datetime.datetime.now().hour
  print(current_hour)
  if current_hour < 12:
      return "Good morning! Have a wonderful day ahead."
  elif 12 <= current_hour < 17:
    return "Good afternoon! Hope you're having a great day."
  elif 17 <= current_hour < 20:
    return "Good evening! Wishing you a peaceful evening."
  else:
    return "Good night! Have a restful sleep."


