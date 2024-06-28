
import math

import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import re

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[0].id)

# message=['time','tell me about','temperature is high','body temperature',
#          'long term cough', 'swelling','feeling very thirsty','extreme bleeding']

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def extract_integer(text):
    match=re.search(r'\b\d+\b',text)
    if match:
        return int(match.group())
    else:
        return None

def take_command2():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    # except sr.UnknownValueError:
    #     talk("Sorry, I did not understand that.")
    #     return None
    # except sr.RequestError as e:
    #     talk("Could not request results; {0}".format(e))
    #     return None
    except Exception as e:
        print("Error: ", e)
        return None


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("I am Doctor AI, how can i assist you?")
            talk("I am Doctor Ai, How can i assist you?")

            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'doctor' in command:
                command = command.replace('doctor', '').strip()
                return command
            else:
                return command
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
        return None
    except sr.RequestError as e:
        talk("Could not request results; {0}".format(e))
        return None
    except Exception as e:
        print("Error: ", e)
        return None



def run_alexa():
    command = take_command()
    if command:
        print(f"Command received: {command}")  # Debug: Print the command
 #to know Time
        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)


# to know about something
        elif 'tell me about' in command:
            look_for = command.replace('tell me about', '').strip()
            info = wikipedia.summary(look_for, 1)
            print(info)
            talk(info)
#lungs diseases
        elif 'long term cough' in command:
            print('Is your body temperature is high?')
            talk('is your body temperature is high?')
            take = take_command2()
            print(take)
            if 'yes' in take:
                print("Are you getting weight loss?")
                talk("Are you getting weight loss?")
                take = take_command2()
                if 'yes' in take:
                    print("you should talk to pulmonologist")
                    talk('you should talk to pulmonologist')
                elif 'no' in take:
                    print('at first you should identify your syndrome')
                    talk('at first you should identify your syndrome')
            # kidney diseases
        elif "swelling" in command:
            print("Do you feel tiredness?")
            talk('do you feel tiredness?')
            take = take_command2()
            if 'yes' in take:
                print("swilling around eyes and ankles?")
                talk("swilling around eyes and ankles?")
                take = take_command2()
                if 'yes' in take:
                    print("Your might be chronic kidney diseases.")
                    talk('your might be chronic kidney diseases.')
                elif 'no' in take:
                    print('it is out of my knowledge')
                    talk('it is out of my knowledge')
            # diabetes
        elif "feeling very thirsty" in command:
            print('Are you feeling tired all the time? ')
            talk('are you feeling tired all the time? ')
            take = take_command2()
            if 'yes' in take:
                print("Please test your suger level.")
                talk("Please test your suger level.")
            else:
                print("It is out of my knowledge.")

            # blood cancer
        elif 'extreme bleeding' in command:
            print('Are your swelling')
            talk('are your swelling')
            take = take_command2()
            if 'yes' in take:
                print("do you have shortness of breath?")
                talk("do you have shortness of breath?")
                take = take_command2()
                if 'yes' in take:
                    print("you should talk to a haematologist")
                    talk("you should talk to a haematologist")
                elif 'no' in command:
                    print("you should test your blood")
                    talk("you should test your blood")
                else:
                    talk('i did not understand you.would i search it in google?')
                    take = take_command2()
                    if 'yes' in take:
                        s = "I am searching for you."
                        print(s)
                        talk(s)
                        pywhatkit.search("why extreme bleeding occurred")
                    else:
                        return

        elif "medicine suggestion" in command:
            print("How can i suggest you?")
            talk("How can i suggest you?")
            take = take_command2()
            st = wikipedia.search(take, 2)
            print(st)
            talk(st)

        elif "can you calculate my bmi" in command:
            talk("yes i am able to calculate your bmi."
                 "Please tell your weight in kg. ")
            weight = int(take_command2())
            talk("Please enter your height in centimetre.")
            height = int(take_command2())

            result = (weight / (height * height))*10000
            print(f"Your BMI result is {result}")
            talk(f"Your BMI result is {result}")  
        else:
            talk('I did not understand you. Could i search it google?')
            take = take_command2()
            if 'yes' in take:
                s = "I am searching for you."
                print(s)
                talk(s)
                pywhatkit.search(command)


run_alexa()
