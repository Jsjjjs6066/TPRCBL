from TPRCBL.parser.page import Page
from TPRCBL.parser.pPage import ParsedPage
from TPRCBL.elements import *

def parse(code: Page) -> ParsedPage:
    return ParsedPage(code.code.get('title'))