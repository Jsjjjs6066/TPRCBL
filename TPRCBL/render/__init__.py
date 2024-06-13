from render.title import setTitle

def render(page) -> str:
    txt: str = ''
    for i in page.elements:
        txt += i.render()
    print(txt)
    setTitle(page.title)
    return txt
