from stt_config import stt

def transcribe_audio(audio_file_name='audio.wav'):

  with open(audio_file_name, 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel', continuous=True).get_result()

  text = [result['alternatives'][0]['transcript'].rstrip() + '.\n' for result in res['results']
  text = [para[0].title() + para[1:] for para in text]
  transcript = ''.join(text)
    with open('transcript.txt', 'w') as out:
      out.writeline(transcript)

