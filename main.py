from PIL import Image, ImageDraw

page_1 = Image.new('RGB', (2480, 3508))
page_2 = Image.new('RGB', (2480, 3508))
image_1 = Image.new('RGB', (2480/2, 3508/2), color = 'green')
image_2 = Image.new('RGB', (2480/2, 3508/2), color = 'yellow')
image_3 = Image.new('RGB', (2480/2, 3508/2), color = 'red')
image_4 = Image.new('RGB', (2480/2, 3508/2), color = 'orange')
image_5 = Image.new('RGB', (2480/2, 3508/2), color = 'black')
image_6 = Image.new('RGB', (2480/2, 3508/2), color = 'white')
image_7 = Image.new('RGB', (2480/2, 3508/2), color = 'purple')
image_8 = Image.new('RGB', (2480/2, 3508/2), color = 'pink')

# d1 = ImageDraw.Draw(page_1)
# d2 = ImageDraw.Draw(page_2)
# d1.text((10,10), "Hello world", fill=(255,255,0))
# d2.text((10,10), "Hello world", fill=(255,255,0))

page_1.paste(image_1, (0, 0))
page_1.paste(image_2, (1240, 0))
page_1.paste(image_3, (0, 1754))
page_1.paste(image_4, (1240, 1754))
page_2.paste(image_5, (0, 0))
page_2.paste(image_6, (1240, 0))
page_2.paste(image_7, (0, 1754))
page_2.paste(image_8, (1240, 1754))

page_1.save("flashcards.pdf", "PDF", resolution=300.0, save_all=True, append_images=[page_2])
