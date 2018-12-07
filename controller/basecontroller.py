# Base abstract class for controller


class BaseController:
    def __init__(self):
        pass

    def set_control(self,**kwargs):
        raise NotImplemented("Function not implemented")

    def _exec(self,key):
        raise NotImplemented("Function not implemented")

    def start(self):
        raise NotImplemented("Function not implemented")

