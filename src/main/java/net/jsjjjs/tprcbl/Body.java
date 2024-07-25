package net.jsjjjs.tprcbl;

import net.jsjjjs.tprcbl.elements.Element;

public class Body {
    private Element[] elements;

    public Body(Element[] elements) {
        this.elements = elements;
    }

    public Element[] getElements() {
        return elements;
    }
    public void setElements(Element[] newElements) {
        this.elements = newElements;
    }
}
