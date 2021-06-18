import speech_recognition as sr
import os.path
from os import path
from pydub import AudioSegment
from pydub.silence import split_on_silence
import keyboard
from pydub import AudioSegment
from pydub.playback import play

from chores import think

r = sr.Recognizer()



class chore():
    def executechore(transcript):
        print("Executing .."+transcript)
        if "open Firefox" in transcript:
            print("opening firefox")
            os.system("firefox")
        return

    def executesudochore(transcript):
        print("Executing as sudo.."+transcript)
        return

def open(chore):
    if str(chore) == "open Firefox":
        print("opening firefox")
        os.system("firefox")

def insult(chore):
    if "f****** b****" in chore:
        voice = AudioSegment.from_mp3('src/library/fuckyou.mp3')
        play(voice)
        

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
 

    
    # path = "src/tmp/tempreceive.wav"
    # isdir = os.path.isfile(path)
    # if isdir == True:
    try:    
        transcript = save_audio()
        print("[INPUT RECIEVED]:", transcript)
        
        trigger = "assistant"
        sudo_trigger = "sudo penis"
        chore = save_audio()
        if trigger in chore:
            voice = AudioSegment.from_mp3('src/library/greeting.mp3')
            play(voice)
            # chore.executechore(chore)
            # insult(chore)
            try:
                transcript = save_audio()
                think(transcript)
                # if transcript == "you suck penis":
                #     voice = AudioSegment.from_mp3('src/library/fuckyou.mp3')
                #     play(voice)
            except:
                noaudio = True
        # if len(chore) < 0 and :
        #     chore.executechore(chore)
        
    except:
        noaudio = True
        


        #continuously listen for trigger to access sudo commands
    # print("transcript  "+transcript)
    

    # if trigger in transcript:
    #     print("Keyword heard")
    #      #alternative to 'hey google' 
    #     voice = AudioSegment.from_mp3('src/library/greeting.mp3')
    #     play(voice)
    #     try:
    #         save_audio()
    #     except:
    #         replaysound("src/library/noinput.mp3")

    #         # isdir = os.path.isfile(path)
    #         # if isdir == True:
    #             # transcript = recognize_audio()
    #     chore.executechore(transcript)
               

    #         #------------------------------------------------------------------      

    # elif sudo_trigger in transcript:
    #     playsound('src/library/greeting.mp3')
    #     try:
    #         save_audio()
    #     except:
    #         replaysound("src/library/noinput.mp3")
        
    #     isdir = os.path.isfile(path)
    #     if isdir == True:
    #         transcript = recognize_audio()
    #         executesudochore(transcript)
                
