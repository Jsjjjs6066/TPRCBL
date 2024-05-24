from sys import argv
import sys

import json

from render import render
from elements import *

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

def file(path: str) -> Page:
    with open(path, 'r') as f:
        d: str = f.read()
        return Page(json.loads(d))


page: Page = file(argv[1])
decoded: ParsedPage = page.decode()

render(decoded)

try:
    while True: pass
except KeyboardInterrupt:
    print('Exited TPRCBL')
