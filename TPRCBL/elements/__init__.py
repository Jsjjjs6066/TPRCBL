class Element:
    def __init__(self, innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
        self.innerTPRCBL = innerTPRCBL
        self.args = args
    def render():
        pass

class Para(Element):
    def __init__(self, innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
        super().__init__(innerTPRCBL, args)
    def render(self):
        if type(self.innerTPRCBL) == type(''):
            print(self.innerTPRCBL)

# class Head(Para):
#     def __init__(self, innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
#         super().__init__(innerTPRCBL, args)
#     def render(self):

class NL(Para):
    def __init__(self, args: dict = {}) -> None:
        super().__init__('', args)
    def render(self):
        return super().render()
