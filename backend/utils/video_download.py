import validators

def download(video_link):

  if validators.url(video_link):

    r = requests.get(video_link, stream = True)

    with open('temp', 'wb') as f:
        for chunk in r.iter_content(chunk_size = 360*360):
            if chunk:
                f.write(chunk)

    print("video download complete!")

    return

  else: print("invalid url!")

  return
