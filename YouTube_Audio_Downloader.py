import os
def YouTube_Audio_Downloader():
	Downloading = True
	program = True
	while program == True:
		import os
		print("\nWelcome to YouTube Audio Downloader! \n")
		save_path = input("Enter the path of the folder where you want to download the file:")
		if os.path.exists(save_path):
			while Downloading==True:
				from pytube import YouTube
				from  pytube import Playlist
				import os
							
				flag = True
				while flag == True:
					Amount = input("\nFor only one video press 1 while for whole playlist press 2: ")
					if Amount == "1" or Amount == "2":
						flag = False 
					else:
						print("\nInvalid input! Please try again!")
				if Amount == "1":
					URL = YouTube(input("\nEnter the URL link of the video whose audio you want to download: "))
					print("Downloading: {0}".format(URL.title))
					Type = URL.streams.filter(type="audio").first().download(save_path)
					print("Your download is complete!")
				else:
					URL = Playlist(input("Enter the URL link of the playlist whose audio you want to download: "))
					print("Downloading: {0}".format(URL.title))
					for video in URL.videos:
						video.streams.filter(type="audio").first().download(save_path)
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
		else:
			print("The entered path does not exist. Please try again with a valid path!")
YouTube_Audio_Downloader()
