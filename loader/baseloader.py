
# File containing the Base class for Loader.


class BaseLoader:

    def __init__(self):
        pass

    def next(self):
        raise NotImplemented("Function to get next image")

    def prev(self):
        raise NotImplemented("Function to get previous image")

    def __len__(self):
        raise NotImplemented("len Function")

    def __getitem__(self, item):
        raise NotImplemented("Get item function")

