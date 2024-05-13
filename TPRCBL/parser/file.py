from TPRCBL.parser.page import Page

def file(path: str) -> Page :
    with open(path, 'r') as f:
        return Page(dict(f.read()))
