# app/core/exceptions.py


class RidePlatformException(Exception):
    def __init__(self, message: str, code: str):
        self.message = message
        self.code = code
