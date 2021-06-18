import speech_recognition as sr
import os.path
from os import path
from pydub import AudioSegment
from pydub.silence import split_on_silence
import keyboard
from playsound import playsound
from chores import *

r = sr.Recognizer()

def recognize_audio():
    sound = AudioSegment.from_wav("src/tmp/tempreceive.wav")
    chunks = split_on_silence(sound, min_silence_len = 500, silence_thresh = sound.dBFS-14, keep_silence = 500)
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""

    #process chunks
    with sr.AudioFile(chunk_filename) as source:
        audio_listened = r.record(source)
        try:
            text = r.recognize_google(audio_listened)
        except sr.UnknownValueError as e:
            print("Error: ", str(e))
        else:
            text = f"{text.capitalize()}."
            print(chunk_filename, ":", text)
            whole_text += whole_text
    os.system("del src/tmp/tempreceive.wav")
    return whole_text


def save_audio():
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=6)
        print("listening...")
        text = r.recognize_google(audio_data)
        # temp_file = open("src/tmp/tempreceive.txt")
        # temp_file.write(text)
        # temp_file.close()
    print(text)
    return text
while True:
    # uinput = input("> ")
    # try:
    #     if uinput == "r":
    #         print("Shortcut Detected! Listening..")
    #         save_audio()
    save_audio()

    
    path = "src/tmp/tempreceive.wav"
    isdir = os.path.isfile(path)
    if isdir == True:
        
        transcript = recognize_audio()
        print("[INPUT RECIEVED]:", transcript)


        #continuously listen for trigger to access sudo commands
        trigger = "hey bitch"
        sudo_trigger = "sudo bitch"

        if trigger in transcript:
             #alternative to 'hey google' 
            playsound('src/library/greeting.mp3')
            try:
                save_audio()
            except:
                replaysound("src/library/noinput.mp3")

            isdir = os.path.isfile(path)
            if isdir == True:
                transcript = recognize_audio()
                chore.executechore(transcript)
                

            #------------------------------------------------------------------      

        elif sudo_trigger in transcript:
            playsound('src/library/greeting.mp3')
            try:
                save_audio()
            except:
                replaysound("src/library/noinput.mp3")
            
            isdir = os.path.isfile(path)
            if isdir == True:
                transcript = recognize_audio()
                executesudochore(transcript)
                
