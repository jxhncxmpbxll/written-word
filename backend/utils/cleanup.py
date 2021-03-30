import os

def delete_temp():
  if os.path.exists("temp.mp4"):
    os.remove("temp.mp4")
    os.remove("audio.wav")
    print "temporary files deleted"
  else:
    print("The file does not exist")