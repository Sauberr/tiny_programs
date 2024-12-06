import pytube

try:
    link = 'your link'
    yt = pytube.YouTube(link)
    new_link = yt.streams.get_highest_resolution().download()
    print('Downloaded: ', new_link)
except pytube.exceptions.RegexMatchError:
    print('Error, write the correct link')
