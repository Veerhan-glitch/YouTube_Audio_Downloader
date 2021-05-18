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
			print("Downloading: {0}".format(URL.title))
			Type = URL.streams.filter(type="audio").first().download()
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