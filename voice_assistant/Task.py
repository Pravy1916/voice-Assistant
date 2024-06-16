import datetime
import os
# from Speak import Say
import sympy
import pyjokes 
import pyautogui
import time
from feautures import *

#time function
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    # Say(time)
    return time

def Date():
    date = datetime.date.today()
    # Say(date)
    return date
def Day():
    day = datetime.datetime.now().strftime("%A")
    # Say(day)
    return day

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        return Time()
    
    elif "date" in query:
        return Date()
    
    elif "day" in query:
        return Day()
    
    elif "joke" in query:
        joke= pyjokes.get_joke()
        # Say(joke)
        return joke


def InputExecution(tag, query):
    print("input working")

    try:
        if "wikipedia" in tag:
            name = str(query).replace("who is","").replace("about","").replace("what is", "").replace("wikipedia", "")
            import wikipedia
            result = wikipedia.summary(name)
            # Say(result)
            return result
            
# ---------------------------------google and youtube searching-------------------------------------------
        elif "google" in tag:
            query = str(query).replace("google", "")
            query = query.replace("search", "")
            import pywhatkit
            pywhatkit.search(query)

        elif "youtube" in tag:
            try:
                import pywhatkit
                search_query = str(query).replace("in youtube", "").strip()
                search_query = str(query).replace("search", "").strip()
                pywhatkit.playonyt(search_query)
                # Say(f"Here are the search results for {search_query} on YouTube.")
                return f"Here are the search results for {search_query} on YouTube."
            except Exception as e:
                # Say(f"Sorry, I couldn't perform the YouTube search. Error: {str(e)}")
                return f"Sorry, I couldn't perform the YouTube search. Error: {str(e)}"
 


# -----------------------------sending whatsapp message to friend--------------------------------------
        elif "whatsapp" in tag:
            query =str(query)
            expressions_to_remove = ["send whatsapp message to","send what's app message to","push whatsapp message to","send message to","send message"]

            expression = query 
            for expr in expressions_to_remove:
                expression = expression.replace(expr, "")

                expression = expression.strip()
                
            time.sleep(1)
            pyautogui.hotkey('win','s')
            time.sleep(1)
            pyautogui.write('whatsapp')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.hotkey('ctrl','f') 
            pyautogui.hotkey('ctrl','a')
            pyautogui.write(expression)
            time.sleep(2)
            pyautogui.press('down') #x=266, y=236
            pyautogui.press('enter') #x=266, y=236
            time.sleep(2)
            # pyautogui.click(x=1089, y=991) 
            # time.sleep(1)
            pyautogui.write("hello")
            pyautogui.press("enter")
# ------------------------------websites-------------------------------------------------
        elif "website" in tag:
            import webbrowser
            query=str(query)
            query=query.replace("open","")
            query=query.replace("launch","")
            query=query.replace("dot",".")
            query=query.replace("website","")
            query=query.replace(" ","")

            webbrowser.open(f"https://www.{query}")

# ------------------------------songs-----------------------------------------------------------------
        
        elif "songs" in tag:
            query = str(query).replace("play", "")
            music_directory = "C:\\Users\\PRAVEEN\\Music\\songs"
            songs = [file for file in os.listdir(music_directory) if file.endswith('.mp3')]

            if songs:
                # import playsound
                import random
                random_song = random.choice(songs)
                os.startfile(os.path.join(music_directory,random_song))
                
            else:
                # Say("No songs found in the directory.")
                return "NO songs found in the director."
            
# -------------------------installed applications------------------------------------------------
        elif "laptop" in tag:
            expressions_to_remove=["open in laptop","in laptop","in system","open in system"]
            expression = query 
            for expr in expressions_to_remove:
                expression = expression.replace(expr, "")
                expression = expression.strip()
            if expression.startswith("open "):
                expression = expression[len("open "):].strip()
            pyautogui.hotkey('win','s')
            time.sleep(2)
            pyautogui.write(expression)
            time.sleep(2)
            pyautogui.press('enter')

# ------------------------------caluclations-----------------------------------------------------
        elif "math" in tag:
            try:
                
                
                expressions_to_remove = ["calculate", "solve", "math", "compute",]
                expression = query 
                for expr in expressions_to_remove:
                    expression = expression.replace(expr, "")
                expression = expression.strip()

                if any(op in expression for op in ["+", "-", "*", "/"]):
                    if 'x' in expression:
                        expression = expression.replace('x', '*')
                # Basic arithmetic operations
                    result = sympy.sympify(expression)
                    # Say(f"The result is {result}")
                    return f"The result is {result}"

                elif "plus" in expression:
                    # Addition with 'plus' keyword
                    operands = [int(num) for num in expression.replace("plus", "").split()]
                    result = sympy.Add(*operands)
                    # Say(f"The result is {result}")
                    return f"The result is {result}"

                elif "square root" in expression or "sqrt" in expression:
                    try:
                        radicand = float(expression.replace("square root", "").replace("sqrt", "").strip())
                        result = sympy.sqrt(radicand)
                        formatted_result = "{:.2f}".format(result)
                        # Say(f"The result is {formatted_result}")
                        return f"The result is {formatted_result}"
                    except ValueError:
                        # Say("Invalid input for square root")
                        return "Invalid input for square root"

                elif "cube root" in expression or "cbrt" in expression:
                     # Cube root
                    try:
                        radicand = float(expression.replace("cube root", "").replace("cbrt", "").strip())
                        result = sympy.cbrt(radicand)
                        formatted_result = "{:.2f}".format(result)
                        # Say(f"The result is {formatted_result}")
                        return f"The result is {formatted_result}"
                    except ValueError:
                        # Say("Invalid input for cube root")
                        return "Invalid input for cube root"

                elif any(op in expression for op in ["multiply", "into","x"]):
                    # Multiplication
                    operands = [int(num) for num in expression.replace("multiply", "").replace("into", "").split()]
                    result = sympy.Mul(*operands)
                    # Say(f"The result is {result}")
                    return f"The result is {result}"

                elif any(op in expression for op in ["divide", "divided by"]):
                    # Division
                    operands = [int(num) for num in expression.replace("divide", "").replace("divided by", "").split()]
                    result = sympy.Div(*operands)
                    # Say(f"The result is {result}")
                    return f"The result is {result}"

                elif any(op in expression for op in ["subtract", "subtracted from", "minus"]):
                    # Subtraction
                    operands = [int(num) for num in expression.replace("subtract", "").replace("subtracted from", "").replace("minus", "").split()]
                    result = sympy.Add(*operands)
                    # Say(f"The result is {result}")
                    return f"The result is {result}"

                else:
                    raise ValueError("Unsupported mathematical expression")

            except Exception as e:
                # Say(f"Sorry, I couldn't calculate that. Please provide a valid mathematical expression.")
                return f"Sorry, I couldn't calculate that. Please provide a valid mathematical expression."

#-------------------------------------voice type------------------------------------------------
        
        elif "voice type" in tag:
            result=VoiceType()
            return result
             
        elif "weather" in tag:
            result=weather(query)
            return result
        
        elif "hai" in tag:
            result=wishes()
            print("wishes working") 
            return result
        

        
        elif "helping mode" in tag:
            # print("cooking")
            print(query,"query")
            expression=query
            expression=expression.replace("activate helping mode and say","")
            expression=expression.replace("start helping mode and say","")
            max_result=1
            how_to=search_wikihow(expression,max_result)
            assert len(how_to)==1
            # print(how_to[0].summary)
            return how_to[0].summary    #it says every step in every 25 seconds in front end




    except Exception as e:
        # Handle the exception, you can print the error message or log it
        print(f"An error occurred: {e}")
        # Say("Sorry, I encountered an error while processing your request.")
        return "Sorry, I encountered an error while processing your request."



