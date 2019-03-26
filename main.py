from textwrap import fill
from csv import reader
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from math import ceil

w, h = 2480, 3508 # The width and height of an A4 piece of paper in pixels when printed at 300 dpi (dots per inch)
page_1 = Image.new('RGB', (w, h)) # Creates the first A4 sized image
page_2 = Image.new('RGB', (w, h)) # Creates the second A4 sized image

# Creates 8 images to allow for four double sided flashcards

image_1 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_2 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_3 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_4 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_5 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_6 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_7 = Image.new('RGB', (w//2, h//2), (255, 255, 255))
image_8 = Image.new('RGB', (w//2, h//2), (255, 255, 255))

# Configures the 8 images to allow text to be put on them
d1 = ImageDraw.Draw(image_1)
d2 = ImageDraw.Draw(image_2)
d3 = ImageDraw.Draw(image_3)
d4 = ImageDraw.Draw(image_4)
d5 = ImageDraw.Draw(image_5)
d6 = ImageDraw.Draw(image_6)
d7 = ImageDraw.Draw(image_7)
d8 = ImageDraw.Draw(image_8)

# Asks the user what the contents they want on their flashcards

while True:
	answer = input("Enter type or file to select where to get your content from: ")
	if answer == "file":
		break
	elif answer == "type":
		break

keywords = []
definitions = []

if answer == "type":
   	keywords.append(input("Keyword: "))
   	definitions.append(input("Definition: "))
   	keywords.append(input("Keyword: "))
   	definitions.append(input("Definition: "))
   	keywords.append(input("Keyword: "))
   	definitions.append(input("Definition: "))
   	keywords.append(input("Keyword: "))
   	definitions.append(input("Definition: "))

else:
	root = Tk()
	root.filename = filedialog.askopenfilename(initialdir = "/home/pi/", title = "Select file", filetypes = [("csv files", "*.csv")])
	with open(root.filename) as csvfile:
	    	readCSV = reader(csvfile, delimiter=',')
    		for row in readCSV:
        		keyword = row[0]
        		definition = row[1]
        		keywords.append(keyword)
        		definitions.append(definition)

# Allows the flashcards to use everyone favourite font
font_size = int(input("Enter font size: "))
font = ImageFont.truetype("anonymous.ttf", font_size)

# Puts the text entered by the user onto the flashcards
hehe = fill(keywords[0], width=int(w/2/(ceil(font_size/3*2))))
print(hehe)
d1.text((0,0), hehe, fill=(0,0,0), font=font)
#d1.text((10,10), keywords[0], fill=(0,0,0), font=font)
d2.text((10,10), keywords[1], fill=(255,0,127), font=font)
d3.text((10,10), keywords[2], fill=(255,0,255), font=font)
d4.text((10,10), keywords[3], fill=(127,0,255), font=font)
d5.text((10,10), definitions[1], fill=(0,0,255), font=font)
d6.text((10,10), definitions[0], fill=(0,127,255), font=font)
d7.text((10,10), definitions[3], fill=(0,255,255), font=font)
d8.text((10,10), definitions[2], fill=(0,255,127), font=font)

# Pastes the flashcard into the right place on the A4 pages
page_1.paste(image_1, (0, 0))
page_1.paste(image_2, (1240, 0))
page_1.paste(image_3, (0, 1754))
page_1.paste(image_4, (1240, 1754))
page_2.paste(image_5, (0, 0))
page_2.paste(image_6, (1240, 0))
page_2.paste(image_7, (0, 1754))
page_2.paste(image_8, (1240, 1754))

# Saves the PDF
page_1.save("flashcards.pdf", "PDF", resolution=300.0, save_all=True, append_images=[page_2])
