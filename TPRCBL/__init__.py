from sys import path
path.insert(0, 'C:\\leon zlender\\TPRCBL')

from sys import argv
from parser.page import Page
from parser.file import file
from parser.pPage import ParsedPage
from TPRB.render import render

page: Page = file(argv[1])
decoded: ParsedPage = page.decode()

render(decoded)
