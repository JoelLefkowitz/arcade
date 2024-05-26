import javascript


class BaseScene:
    key = "Base"

    def __init__(self, callback=None):
        self.callback = callback

    def preload(self):
        this = javascript.this()
        this.load.setBaseURL("./assets")

    def create(self, *args):
        pass

    def update(self, *args):
        pass

    @property
    def scene(self):
        return {
            "key": self.key,
            "preload": self.preload,
            "create": self.create,
            "update": self.update,
        }
