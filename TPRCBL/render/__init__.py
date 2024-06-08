from render.title import setTitle

def render(page) -> None:
    for i in page.elements:
        i.render()
    setTitle(page.title)
