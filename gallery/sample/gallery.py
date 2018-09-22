import os
import operator
from .thumbnails import create_thumbnails


class Gallery:
    def __init__(self, gallery_path):
        self.image_root = "gallery-images/"
        self.thumb_root = "media/gallery-thumbs/"
        self.gallery_path = gallery_path
        self.subgalleries = []
        self.images = []

        self.__set_images_and_subgalleries(self.image_path())
        create_thumbnails(self.images, self.thumb_path())

    def image_path(self):
        return self.image_root + self.gallery_path

    def thumb_path(self):
        return self.thumb_root + self.gallery_path

    def __set_images_and_subgalleries(self, gallery_path):
        dir_entries = os.scandir(gallery_path)

        for dir_entry in dir_entries:
            if dir_entry.is_dir():
                self.subgalleries.append(dir_entry)
            elif dir_entry.is_file():
                self.images.append(dir_entry)

        self.__sort_entries()

    def __sort_entries(self):
        self.images.sort(key=operator.attrgetter('name'))
        self.subgalleries.sort(key=operator.attrgetter('name'), reverse=True)
