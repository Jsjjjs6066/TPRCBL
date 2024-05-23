from TPRB.render.title import setTitle
from TPRCBL.parser.pPage import ParsedPage

def render(page: ParsedPage) -> None:
    setTitle(page.title)