import os

def cleanup():
  if os.path.exists("temp.mp4"):
    os.remove("temp.mp4")
    os.remove("audio.wav")
  else:
    print("The file does not exist")