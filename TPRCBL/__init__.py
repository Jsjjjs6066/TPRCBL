from sys import argv
from TPRCBL.parser.page import Page
from TPRCBL.parser.file import file

page: Page = file(argv[1])
