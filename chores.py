import os
import sys

#keywords from transcript (triggers)
start_task_triggers = ["firefox", "update", "upgrade", "shutdown", "reboot", "time", "date"]
start_task_commands = ["firefox", "sudo apt update", "sudo apt upgrade -y", "shutdown", "reboot"]

#security triggers/commands:
security_task_triggers = ["start security", "disable security", "read log"]
security_task_commands = ["cd ~/security && ./startall", "cd ~/security && ./stopall", "cd ~/security && python3 readlog.py"]

def think(transcript):
    print("thinking.. "+transcript)
    words = transcript.split()
    print("Words: "+ words)
    

    for word in words:
        try:
            for trigger in start_task_triggers:
                if word == trigger:
                    print(word+" is equal to a trigger: \""+trigger+"\"")
                    index = start_task_triggers.index(word)
                    os.system(start_task_commands[index])
        except:
            for trigger in security_task_triggers:
                if word == trigger:
                    print(word+" is equal to a trigger: \""+trigger+"\"")
                    index = security_task_triggers.index(word)
                    os.system(security_task_commands[index])
        







# messaging_task_triggers = []
# messaging_task_commands = []

    
