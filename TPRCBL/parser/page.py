from TPRCBL.parser import parse
from TPRCBL.parser.pPage import ParsedPage

class Page:
    def __init__(self, code: dict[str, dict]) -> None:
        self.code = code
    def decode(self) -> ParsedPage:
        return parse(self)
