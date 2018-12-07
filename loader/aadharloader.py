import os

import cv2

from loader.baseloader import BaseLoader


class AadharLoader(BaseLoader):

    def __init__(self, folderpath):
        '''Initialized pos and list of image files.

        Args:
            folderpath:
        '''
        super().__init__()
        self.folderpath = folderpath
        self.files = []
        for f in os.scandir(folderpath):
            filepath = os.path.join(f.path, 'face_1.jpg')
            if os.path.exists(filepath) and os.path.isfile(filepath):
                self.files.append(filepath)

        self.pos = 0

    def next(self):
        '''Gets next frame.

        Returns:
            cv2 image

        '''
        assert(self.pos >= 0)
        assert(self.pos < len(self.files))
        img = cv2.imread(self. files[self.pos])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.pos += 1
        return img

    def prev(self):
        '''Gets previous frame.

        Returns:
            cv2 image

        '''
        self.pos -= 1
        return self.next()

    def __len__(self):
        return len(self.files)

    def __getitem__(self, item):
        img = cv2.imread(self.files[item])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

