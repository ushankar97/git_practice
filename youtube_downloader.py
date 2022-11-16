from pytube import YouTube
yt = YouTube("https://youtu.be/VhAqAa0eUkw")
yt = yt.get('mp4', '720p')
yt.download('C:\\dacument')