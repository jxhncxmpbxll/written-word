import asyncio

from utils import cleanup, extract_audio, transcribe_audio, video_download

async def dl(link):
  # print("downloading video")
  # await video_download.download(link)
  # await extract_and_transcribe()
  return link

async def extract_and_transcribe():
  print("extracting audio")
  await extract_audio.extract()
  print("transcribing audio")
  await transcribe_audio.transcribe()
  print("deleting temporary files")
  await cleanup.delete_temp()

