from os import get_terminal_size

class Element:
    def __init__(self, innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
        self.innerTPRCBL = innerTPRCBL
        self.args = args
    def render(self):
        return ''

class Para(Element):
    def __init__(self, innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
        super().__init__(innerTPRCBL, args)
    def render(self):
        if type(self.innerTPRCBL) == type(''):
            return self.innerTPRCBL + '\n'

# class Head(Para):
#     def __init__(self, innerTPRCBL: dict | str | None = None, args: dict = {}) -> None:
#         super().__init__(innerTPRCBL, args)
#     def render(self):

class Line(Element):
    def __init__(self, char: str = ' ', args: dict = {}) -> None:
        if len(char) == 1:
            super().__init__(char, args)
        else:
            super().__init__(char[0], args)
    def render(self):
        if self.args.get('height') != None:
            if self.args.get('height') >= 1:
                return ((self.innerTPRCBL * get_terminal_size().columns) + '\n') * self.args.get('height')
            else:
                return (self.innerTPRCBL * get_terminal_size().columns) + '\n'
        else: 
            return (self.innerTPRCBL * get_terminal_size().columns) + '\n'

class NL(Line):
    def __init__(self, args: dict = {}) -> None:
        super().__init__(' ', args)
    def render(self):
        return super().render()
