from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=pqmEo23J6LE')
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
stream.download(filename='video.mp4')


