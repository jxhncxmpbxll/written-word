import subprocess

def extract():
  command = "ffmpeg -i temp.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
  subprocess.call(command, shell=True)

  print("audio extracted!")