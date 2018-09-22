import os
from PIL import Image, ImageOps


THUMBNAIL_SIZE = (200, 200)


def create_thumbnails(images, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    for image in images:
        if image.name not in os.listdir(destination_path):
            picture = Image.open(image.path)
            thumb = ImageOps.fit(picture, THUMBNAIL_SIZE, Image.ANTIALIAS)

            thumb.save(destination_path + image.name)
