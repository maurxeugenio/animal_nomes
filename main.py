import csv
import cv2
import requests
import numpy as np
from random import randint
from PIL import ImageFont, ImageDraw, Image


with open('nomes_reduzidos.csv', newline='') as csvfile:
    list_names = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in list_names:
        img_request = requests.get('https://randomfox.ca/floof/').json()['image']

        img_data = requests.get(img_request).content

        name = ' '.join(row)
        image_path = f'downloads/{name}.jpg'

        with open(image_path, 'wb') as handler:
            handler.write(img_data)

        image = cv2.imread(image_path)


        cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb)

        draw = ImageDraw.Draw(pil_im)

        fonts = ['Comics-Sans.ttf', 'Roboto-Regular.ttf']
        font = ImageFont.truetype(fonts[randint(0, 1)], 50)

        position = [(randint(0, pil_im._size[0]) / 2 ), (randint(0, pil_im._size[1]) / 2 )]

        draw.text((position[0], position[1]), name, font=font)

        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        cv2.imwrite(f"resultados/{name}.png", cv2_im_processed)
