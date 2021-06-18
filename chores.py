

class chore():
    def executechore(transcript):
        print("Executing .."+transcript)
        if "open Firefox" in transcript:
            os.system("firefox")
        return

    def executesudochore(transcript):
        print("Executing as sudo.."+transcript)
        return
