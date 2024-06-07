from sys import argv
from os import get_terminal_size, system
from msvcrt import getwch

import json

from render import render
from render.title import setTitle
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
    elems: list[Element] = []
    for i in code.code.get('body'):
        if i[0] == 'para':
            if len(i) == 2:
                elems.append(Para(i[1]))
            else:
                elems.append(Para(i[1]), i[2])
        if i[0] == 'nl':
            if len(i) == 2:
                elems.append(NL(i[1]))
            else:
                elems.append(NL())
    return ParsedPage(code.code.get('title'), elems)

def file(path: str) -> Page:
    with open(path, 'r') as f:
        d: str = f.read()
        return Page(json.loads(d))

def load():
    system('cls')
    page: Page = file(argv[1])
    setTitle('Parsing loaded file...')
    decoded: ParsedPage = page.decode()

    setTitle('Rendering loaded parsed file...')
    render(decoded)

if __name__ == '__main__':
    if len(argv) >= 2:
        setTitle('Loading from file...')
        load()
        try:
            while True: 
                inp: str = getwch()
                if inp.lower() == 'x':
                    system('cls')
                    print('Exited TPRCBL', end='')
                    exit()
                if inp.lower() == 'r':
                    load()
        except KeyboardInterrupt:
            print('Exited TPRCBL', end='')
