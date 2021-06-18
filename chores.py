
def think(transcript):
    print("thinking.. "+transcript)
    words = transcript.split()
    print(splits)
    for word in words:
        if word.lower() == "firefox":
            os.system("firefox")
    
