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
        match i[0]:
            case 'para':
                if len(i) == 2:
                    elems.append(Para(i[1]))
                else:
                    elems.append(Para(i[1]), i[2])
            case 'nl':
                if len(i) == 2:
                    elems.append(NL(i[1]))
                else:
                    elems.append(NL())
            case 'line':
                if len(i) == 3:
                    elems.append(Line(i[1], i[2]))
                else:
                    elems.append(Line(i[1]))
    return ParsedPage(code.code.get('title'), elems)

def file(path: str) -> Page:
    with open(path, 'r') as f:
        d: str = f.read()
        return Page(json.loads(d))

def load() -> str:
    system('cls')
    page: Page = file(argv[1])
    setTitle('Parsing loaded file...')
    decoded: ParsedPage = page.decode()

    setTitle('Rendering loaded parsed file...')
    return render(decoded)

def clr() -> None:
    system('cls')

def x(txt: str) -> None:
    clr()
    print('Do you want to exit TPRCBL? (Y/N)')
    while True:
        yn: str = getwch()
        if yn.lower() == 'y':
            clr()
            print('Exited TPRCBL', end='')
            exit()
        if yn.lower() == 'n':
            clr()
            print(txt)
            break

if __name__ == '__main__':
    if len(argv) >= 2:
        setTitle('Loading from file...')
        txt: str = load()
        try:
            while True: 
                inp: str = getwch()
                if inp.lower() == 'x':
                    x(txt)
                if inp.lower() == 'r':
                    txt: str = load()
        except KeyboardInterrupt:
            print('Exited TPRCBL', end='')
