import os
import operator
from .thumbnails import create_thumbnails
from .breadcrumbs import create_breadcrumbs


FILE_TYPES = ('.jpg', '.jpeg', '.png', '.gif')


class Gallery:
    def __init__(self, gallery_path, gallery_web_path):
        self.image_root = "gallery-images/"
        self.thumb_root = "media/gallery-thumbs/"
        self.gallery_path = gallery_path
        self.subgalleries = []
        self.images = []

        self.__set_images_and_subgalleries(self.image_path())
        self.breadcrumbs = create_breadcrumbs(self.gallery_path, gallery_web_path)
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
            elif dir_entry.is_file() and dir_entry.name.endswith(FILE_TYPES):
                self.images.append(dir_entry)

        self.__sort_entries()

    def __sort_entries(self):
        self.images.sort(key=operator.attrgetter('name'))
        self.subgalleries.sort(key=operator.attrgetter('name'), reverse=True)

    def __str__(self):
        if self.gallery_path == "":
            return "Galleria"
        else:
            return os.path.basename(os.path.dirname(self.image_path() + "/"))
