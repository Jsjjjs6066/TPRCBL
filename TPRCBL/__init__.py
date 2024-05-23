# from sys import path
# path.insert(0, 'C:\\leon zlender\\TPRCBL')

from sys import argv
# from parser.page import Page
# from parser.file import file
# from parser.pPage import ParsedPage
from render import render
from TPRCBL.elements import *


class ParsedPage:
    def __init__(self, title: str = 'Page', elenents: list[Element] = []) -> None:
        self.title = title
        self.elements = elenents

class Page:
    def __init__(self, code: dict[str, dict]) -> None:
        self.code = code
    def decode(self) -> ParsedPage:
        return parse(self)

def parse(code: Page) -> ParsedPage:
    return ParsedPage(code.code.get('title'))

def file(path: str) -> Page :
    with open(path, 'r') as f:
        return Page(dict(f.read()))

page: Page = file(argv[1])
decoded: ParsedPage = page.decode()

render(decoded)
