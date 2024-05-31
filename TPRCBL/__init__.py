from sys import argv
from os import get_terminal_size
from msvcrt import getwch

import json

from render import render
from render.title import setTitle
from elements import *

setTitle('Loading from file...')
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
    elems: list[Element] = []
    for i in code.code.get('body'):
        if i[0] == 'para':
            if len(i) == 2:
                elems.append(Para(i[1]))
            else:
                elems.append(Para(i[1]), i[2])
    return ParsedPage(code.code.get('title'))

def file(path: str) -> Page:
    with open(path, 'r') as f:
        d: str = f.read()
        return Page(json.loads(d))

def load():
    page: Page = file(argv[1])
    setTitle('Parsing loaded file...')
    decoded: ParsedPage = page.decode()

    setTitle('Rendering loaded parsed file...')
    render(decoded)

if __name__ == '__main__':
    load()
    try:
        while True: 
            inp: str = getwch()
            if inp.lower() == 'x':
                print('Exited TPRCBL', end='')
                exit()
            if inp.lower() == 'r':
                print('\n' * get_terminal_size().lines)
                load()
    except KeyboardInterrupt:
        print('Exited TPRCBL', end='')
