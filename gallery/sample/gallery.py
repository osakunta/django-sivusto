import os


class Gallery:
    def __init__(self, gallery_path):
        self.image_root = "gallery-images/"
        self.thumb_root = "media/gallery-thumbs/"
        self.gallery_path = gallery_path
        self.subgalleries = []
        self.images = []

        self.__set_images_and_subgalleries(self.absolute_gallery_path())

    def absolute_gallery_path(self):
        return self.image_root + self.gallery_path

    def absolute_gallery_thumbs(self):
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
        self.images.sort()
        self.subgalleries.sort(reverse=True)
