from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap

w, h = 2480, 3508 # The width and height of an A4 piece of paper in pixels when printed at 300 dpi (dots per inch)
page_1 = Image.new('RGB', (w, h)) # Creates the first A4 sized image
page_2 = Image.new('RGB', (w, h)) # Creates the second A4 sized image

# Creates 8 images to allow for four double sided flashcards

image_1 = Image.new('RGB', (w//2, h//2))
image_2 = Image.new('RGB', (w//2, h//2))
image_3 = Image.new('RGB', (w//2, h//2))
image_4 = Image.new('RGB', (w//2, h//2))
image_5 = Image.new('RGB', (w//2, h//2))
image_6 = Image.new('RGB', (w//2, h//2))
image_7 = Image.new('RGB', (w//2, h//2))
image_8 = Image.new('RGB', (w//2, h//2))

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
f1_word = input("Word: ")
f1_def = input("Definition: ")
f2_word = input("Word: ")
f2_def = input("Definition: ")
f3_word = input("Word: ")
f3_def = input("Definition: ")
f4_word = input("Word: ")
f4_def = input("Definition: ")

# Allows the flashcards to use everyone favourite font
font = ImageFont.truetype("comic_sans_ms.ttf", 30)

# Puts the text entered by the user onto the flashcards
d1.text((10,10), f1_word, fill=(255,255,255), font=font)
d2.text((10,10), f2_word, fill=(255,0,127), font=font)
d3.text((10,10), f3_word, fill=(255,0,255), font=font)
d4.text((10,10), f4_word, fill=(127,0,255), font=font)
d5.text((10,10), f2_def, fill=(0,0,255), font=font)
d6.text((10,10), f1_def, fill=(0,127,255), font=font)
d7.text((10,10), f4_def, fill=(0,255,255), font=font)
d8.text((10,10), f3_def, fill=(0,255,127), font=font)

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
