import asyncio

from utils import cleanup, extract_audio, transcribe_audio, video_download

async def dl(link):
  print "downloading"
  await video_download.download(link)
  await extract_and_transcribe()

async def extract_and_transcribe():
  print "extracting audio"
  await extract_audio.extract()
  print "transcribing"
  await transcribe_audio.transcribe()
  print "deleting temporary files"
  await cleanup.delete_temp()
