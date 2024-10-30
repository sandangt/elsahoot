class ItemNotFoundError(Exception):
    def __init__(self, message: str):
        self.message = message


class WriteItemError(Exception):
    def __init__(self, message: str):
        self.message = message
