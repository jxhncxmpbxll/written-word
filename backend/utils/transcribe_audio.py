from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from .auth import api_key, url

def transcribe():

  authenticator = IAMAuthenticator(get_api_key())
  stt = SpeechToTextV1(authenticator=authenticator)
  stt.set_service_url(get_url())

  with open('audio.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel', continuous=True).get_result()

    text = [result['alternatives'][0]['transcript'].rstrip() + '.\n' for result in res['results']]
    text = [para[0].title() + para[1:] for para in text]
    transcript = ''.join(text)
    with open('transcript.txt', 'w') as out:
      out.writeline(transcript)

      print("transcription complete!")

