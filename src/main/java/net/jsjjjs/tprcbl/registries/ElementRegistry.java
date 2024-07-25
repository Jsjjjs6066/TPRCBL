package net.jsjjjs.tprcbl.registries;

import net.jsjjjs.tprcbl.elements.Element;
import net.jsjjjs.tprcbl.elements.Label;

public enum ElementRegistry {
    LABEL(Label.class);

    private final Class<? extends Element> elementClass;

    ElementRegistry(Class<? extends Element> elementClass) {
        this.elementClass = elementClass;
    }

    public Class<? extends Element> getElementClass() {
        return elementClass;
    }
}
