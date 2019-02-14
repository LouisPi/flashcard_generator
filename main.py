from PIL import Image

page_1 = Image.open("page_1.png")
page_2 = Image.open("page_2.png")
page_1 = page_1.resize((2480, 3508))
page_2 = page_2.resize((2480, 3508))

page_1.save("page_1.pdf", "PDF", resolution=300.0, save_all=True, append_images=[page_2])
