import os
def YouTube_Audio_Downloader():
	Downloading = True
	while Downloading==True:
		from pytube import YouTube
		from  pytube import Playlist
		print("Welcome to YouTube Audio Downloader!")
		flag = True
		while flag == True:
			Amount = input("For only one video press 1 while for whole playlist press 2: ")
			if Amount == "1" or Amount == "2":
				flag = False 
			else:
				print("Invalid input! Please try again!")
		if Amount == "1":
			URL = YouTube(input("Enter the URL link of the video whose audio you want to download: "))
			streams = URL.streams
			audio_stream = streams.filter(only_audio=True)
			if(len(audio_stream)):
				print("Downloding audio")
				stream = audio_stream.first()
				stream.download()
				filePath = stream.get_file_path()
				[filename, extension] = os.path.splitext(filePath)
				os.rename(filePath, filename + '.mp3')
			else:
				print("No audio streams found. Downloding in video format.")
				streams.first().download()
			print("Your download is complete!")
		else:
			URL = Playlist(input("Enter the URL link of the playlist whose audio you want to download: "))
			print("Downloading: {0}".format(URL.title))
			for video in URL.videos:
				video.streams.filter(type="audio").first().download()
			print("Your download is complete!")
		flag = True
		while flag:
			Again=input("Do you want to download again? (y/n)").lower()
			if Again == 'y':
				Downloading = True
				flag = False
			elif Again == 'n':
				Downloading = False
				print("Thank you for using!.")
				flag = False
			else:
				print("Invalid input! Please try again!")
YouTube_Audio_Downloader()