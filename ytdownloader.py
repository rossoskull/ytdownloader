import requests
from bs4 import BeautifulSoup
import os

def main():
	print("Welcome to Youtube Playlist Downloader v1.0.0 \nThis is a better way to download complete playlists from YouTube.\n")
	url = str(input('Enter the playlist URL : '))
	print("Collecting page data...")
	try:
		source_code = requests.get(url)
		print("Page Downloaded.")
		print("Extracting Links...")
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'html.parser')
		megastr = ""
		for link in soup.find_all('a'):
			x = str(link.get('href'))
			if "watch" in x:
				megastr += 'youtube-dl \"https://www.youtube.com' + x + '\"\n'
		megastr += "pause"
		print("Generating batch file...")
		fw = open('download.bat', 'w')
		fw.write(megastr)
		fw.close
		#break
	except requests.exceptions.MissingSchema:
		print("Insert the URL along with 'https://' or 'http://' and try again.")
		os.system("pause")
		os.system("cls")
		main()
	except requests.exceptions.ConnectionError:
		print("Could not retrieve data from the Internet. Please try again after a connection is established.")
		os.system("pause")
		os.system("cls")
		main()
	finally:
		print("File created successfully.\n\nInstructions:\nMove the 'youtube-dl.exe' and 'download.bat' file in your destination folder, \nDouble-click the batch file to start download.\n\nThank you for using this software :-)\nMade by Jay Mistry.")
		os.system("pause")

main()