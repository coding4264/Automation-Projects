from pytube import YouTube
from sys import argv

link = input("Enter the youtube link here: ")
yt = YouTube(link)

print("Title: ", yt.title)

print("Views :", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('/Users/Jafar/')   # change in the future