import requests
from bs4 import BeautifulSoup
import requests
import os
import time

# This function receives a URL and an HTML tag, parses out the tag, then returnss all tags that were found
def html_parse(site, tag):
    response = requests.get(site)
    soup = BeautifulSoup(response.content, 'lxml')
    tag_list = soup.select(tag)
    return tag_list

# This function tries to create the user specified folder and returns an error if the folder already exists. The function then calls download_images()
def folder_create(images):
	try:
		folder_name = input("Enter Folder Name:- ")
		# folder creation
		os.mkdir(folder_name)
	# if folder exists with that name, ask another name
	except:
		print("Folder Exist with that name!")
		folder_create()
	# image downloading start
	download_images(images, folder_name)

# This function takes a list of image file names and a folder name, goes through a try - except loop to find the possible invisible data in the found elements,
def download_images(images, folder_name):
	# initial count is zero
	count = 0
	# print total images found in URL
	print(f"Total {len(images)} Image Found!")
	# checking if images is not zero
	if len(images) != 0:
		for i, image in enumerate(images):
			try:
				image_link = image["data-srcset"]
			except:
				try:
					image_link = image["data-src"]
				except:
					try:
						image_link = image["data-fallback-src"]
					except:
						try:
							image_link = image["src"]
						except:
							pass
			try:
				r = requests.get(image_link).content
				try:
					# possibility of decode
					r = str(r, 'utf-8')
				except UnicodeDecodeError:
					# After checking above condition, Image Download start
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)
					# counting number of image downloaded
					count += 1
			except:
				pass
		if count == len(images):
			print("All Images Downloaded!")
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

# Get user input and start the first timer
site1 = input('Please enter the first URL. The program will validate the URL, then download all images from the site after a predetermined delay.')
site2 = input('Please enter the second URL. The program will validate the URL, then parse out various tags from the raw HTML after a predetermined delay. ')
time.sleep(10)

# Validate the URL through web request, then run the specified functions
try:
	r = requests.get(site1)
	soup = BeautifulSoup(r.text, 'html.parser')
	images = soup.findAll('img')
	folder_create(images)
except Exception as exc:
    print('The first URL is invalid')

# Start the second timer
time.sleep(20)

# Validate the URL through web request, then run the specified functions
try:
    request = requests.get(site2)
    print(html_parse(site2,'title'))
    print(html_parse(site2,'img'))
    print(html_parse(site2,'time'))
    print(html_parse(site2,'link'))
    print(html_parse(site2,'video'))
except Exception as exc:
    print('The second URL is invalid')



