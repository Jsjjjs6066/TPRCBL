class Element:
    def __init__(self, tag: str = 'frame', innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
        self.tag = tag
        self.innerTPRCBL = innerTPRCBL
        self.args = args