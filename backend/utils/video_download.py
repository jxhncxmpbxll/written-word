def download(video_link):

  r = requests.get(video_link, stream = True)

  with open('temp', 'wb') as f:
      for chunk in r.iter_content(chunk_size = 1024*1024):
          if chunk:
              f.write(chunk)

  print "video download complete!"

return